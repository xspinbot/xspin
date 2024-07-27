from aiogram import types, html
from aiogram.filters import CommandStart
from aiogram.utils.i18n import gettext

from bot.routers import users_commands as router
from bot.decorators import create_session

from db.schemas import UsersTable
from db.config import Session
from db import repository as repo

from bot.keyboards.inline import start


_ = gettext

@router.message(CommandStart())
@create_session
async def start_handler(message: types.Message, session: Session):
    await repo.UsersTableRepository().create_user(
        user_id = message.from_user.id,
        username = message.from_user.username,
        name = message.from_user.full_name,
        session = session
    )

    await message.answer(_(f"""Привет. Это бот для игры в виртуальное казино 🎰

Для просмотра доступных команд - /help

Правила игры — FAQ

Чат для игры — @xSpinGame

А если ты и так все прекрасно знаешь, добавь меня в свою группу 👇"""), reply_markup = start.button())
    