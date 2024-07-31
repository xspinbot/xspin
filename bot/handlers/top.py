from aiogram import types, html
from aiogram.filters import Command
from aiogram.utils.i18n import gettext
from sqlalchemy.orm import Session

from bot.routers import commands as router
from bot.decorators import create_session
from bot.utils.helpful_functions import top_balance
from db import repository as repo

_ = gettext

@router.message(Command("top"))
@create_session
async def top_handler(message: types.Message, session: Session):
    top_rating = await repo.UsersTableRepository().get_top_rating(session=session)
    user = await repo.UsersTableRepository().get_user(user_id=message.from_user.id,
                                                      session=session)
    balance = await repo.UsersTableRepository().get_balance(user_id=message.from_user.id,
                                                            session=session)
    user_top_rating = (
        (
            top_rating.index(
                {
                    'user_id': message.from_user.id, 
                    'name': message.from_user.full_name,
                    'balance': balance
                }
            )
        ) + 1
    )

    text = ""
    num = 0

    for user in top_rating[:10]:
        num += 1
        user_info = html.bold(f"{user['name']} — {top_balance(user['balance'])}")
        text += f"{num}. {user_info} 💰\n"

    text += "\n" + html.bold(
        ((_(f"Ваше место в топе — ") + f"{user_top_rating}") if not balance == 0
         else _("Чтобы узнать свое место в топе, ваш баланс должен быть больше 0."))
    ) + "\n"
    text += html.bold(_(f"Количество пользователей бота — ") + f"{len(top_rating)}")
    
    await message.answer(text)