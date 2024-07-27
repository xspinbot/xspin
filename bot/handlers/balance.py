from aiogram import types, html
from aiogram.filters import Command
from aiogram.utils.i18n import gettext
from sqlalchemy.orm import Session

from bot.routers import commands as router
from db import repository as repo
from bot.decorators import create_session

_ = gettext

@router.message(Command("balance"))
@create_session
async def balance_handler(message: types.Message, session: Session):
    balance = await repo.UsersTableRepository().get_balance(user_id=message.from_user.id,
                                                            session=session)
    await message.reply(_("Ваш баланс: ") + f"{html.bold(balance)} 💰")