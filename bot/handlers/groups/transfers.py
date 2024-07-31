from aiogram import types, html
from aiogram.utils.i18n import gettext
from sqlalchemy.orm import Session

from bot.routers import groups as router
from bot.decorators import create_session
from bot.filters import Text, Chat, ContentType
from db import repository as repo

_ = gettext

@router.message(Chat().is_group(), ContentType(ContentType.TEXT), Text(startswith='!т '))
@create_session
async def transfer_handler(message: types.Message, session: Session):
    text = message.text
    if len(text.split()) == 2:
        try:
            amount = int(text.split()[1])
            to_message = message.reply_to_message
            if to_message:
                to_user = to_message.from_user

                if not to_user.is_bot:
                    if not to_user.id == message.from_user.id:
                        balance = await repo.UsersTableRepository().get_balance(
                            user_id=message.from_user.id, session=session)
                        transfer = await repo.TransfersTableRepository().create_transfer(
                            from_user_id=message.from_user.id,
                            to_user_id=to_user.id,
                            chat_id=message.chat.id,
                            amount=amount,
                            session=session)
                        
                        if transfer['success']:
                            await message.reply(html.bold(
                                _("Трансфер прошел успешно.") + "\n" + _("Текущий лимит: ") + f"{transfer['transfer']}"))
                        else:
                            if transfer['error'] == "Not enough money!":
                                await message.reply(html.bold(
                                     _("Ваш баланс недостаточен! В балансе: ") + f"{balance} 💰"
                                ))
                            elif transfer['error'] == "Limit is full":
                                await message.reply(html.bold(
                                    _("Сумма превысила дневной лимит. Для увеличения лимита введите команду !лимит боту!")
                                ))
                    else:
                        await message.reply(html.bold(
                            _("Вы не можете перевести деньги себе ❌")))
                else:
                    await message.reply(html.bold(
                        _("Вы не можете перевести деньги боту ❌")))
        
        except ValueError:
            await message.reply(html.bold(_("Вы ввели неверную сумму ❌")))