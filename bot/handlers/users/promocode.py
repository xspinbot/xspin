from aiogram import types, html
from aiogram.utils.i18n import gettext
from aiogram.types import LinkPreviewOptions
from aiogram.filters import CommandStart
from sqlalchemy.orm import Session

from bot.decorators import create_session
from bot.misc import bot_settings
from bot.routers import users as router
from bot.filters import Text, Chat, ContentType, Permission
from bot.keyboards.inline import promocode as button

from db import repository as repo


_ = gettext

@router.message(Chat().is_private(), ContentType(ContentType.TEXT), Text(startswith="!промокод "))
@create_session
async def promocode_handler(message: types.Message, session: Session):
    text = message.text

    if len(text.split()) == 2:
        promocode = text.split()[1]
        
        response = await repo.UsedPromocodesTableRepository().use_promocode(
            promocode=promocode, user_id=message.from_user.id, session=session)
        
        if response['success']:
            await message.answer(
                html.bold(_("💸 Вы успешно активировали промокод!")) + "\n\n" +
                html.italic(_("Баланс пополнен на ") + f"{response['cost']} 💰")
            )
        else:
            if response['error'] == "already used":
                await message.answer(html.bold(
                    _("Вы уже использовали этот промокод ❌")
                ))
            elif response['error'] == "invalid promocode":
                await message.answer(html.bold(
                    _("Промокод недействителен ❌")
                ))


@router.message(Chat().is_private(), CommandStart(), 
                lambda message: (len(str(message.text).split()) == 2 and 
                                str(message.text).split()[1].startswith("promocode_")))
@create_session
async def promocode_start_handler(message: types.Message, session: Session):
    text = message.text.split()[1].split("promocode_")

    if len(text) == 2:
        promocode = text[-1]

        response = await repo.UsedPromocodesTableRepository().use_promocode(
            promocode=promocode, user_id=message.from_user.id, session=session)
        
        if response['success']:
            await message.answer(
                html.bold(_("💸 Вы успешно активировали промокод!")) + "\n\n" +
                html.italic(_("Баланс пополнен на ") + f"{response['cost']} 💰")
            )
        else:
            if response['error'] == "already used":
                await message.answer(html.bold(
                    _("Вы уже использовали этот промокод ❌")
                ))
            elif response['error'] == "invalid promocode":
                await message.answer(html.bold(
                    _("Промокод недействителен ❌")
                ))


@router.message(Chat().is_private(), ContentType(ContentType.TEXT), 
                Text(startswith='!создать-промокод '), 
                Permission(permission_classes=[Permission.ADMIN]))
@create_session
async def create_promocode_handler(message: types.Message, session: Session):
    text = message.text

    if len(text.split()) == 4:
        promocode = text.split()[1]
        try:
            cost = int(text.split()[2])
            max_users = int(text.split()[3])

            is_exist = (not (await repo.PromocodesTableRepository().get_promocode(
                promocode=promocode, session=session)) == None)
        
            if not is_exist:
                await repo.PromocodesTableRepository().create_promocode(
                    promocode=promocode, cost=cost, max_users=max_users, session=session)
                await message.reply(
                    (html.bold(
                        _("Промокод успешно сгенерирован ✅")
                    ) + "\n\n" + html.italic(
                        _("Чтобы использовать промокод:")
                    ) + "\n" + html.code(f"!промокод {promocode}"
                    ) + "\n\n" + html.italic(
                        _("Ссылка для активации промокода:")
                    ) + "\n" + f"https://t.me/{bot_settings.name}?start=promocode_{promocode}"), 
                    link_preview_options = LinkPreviewOptions(is_disabled=True),
                    reply_markup = await button.created(promocode=promocode)
                )
            else:
                await message.reply((
                    html.bold(_("Такой промокод уже существует ❌")) + "\n\n" +
                    html.italic(
                        _("⚠️ Если вы удалите промокод и создадите его заново, список тех, кто использовал промокод, будет удален. ⚠️")
                    )
                ),
                reply_markup = await button.already_exists(promocode=promocode))
        except ValueError:
            await message.reply(
                html.bold(_("Вы ввели неверную информацию о промокоде ❌"))
            )

