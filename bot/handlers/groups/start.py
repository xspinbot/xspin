from aiogram import types, html
from aiogram.filters import CommandStart
from aiogram.utils.i18n import gettext

from bot.routers import groups_commands as router
from bot.decorators import create_session
from bot.keyboards.inline import start
from bot.texts import texts as txt
from bot.filters import Chat

from db.schemas import UsersTable
from db.config import Session
from db import repository as repo

from general.choices import AdminType

_ = gettext

@router.message(Chat().is_group(), CommandStart())
@create_session
async def start_group_handler(message: types.Message, session: Session):
    admin = await repo.AdminsTableRepository().get_admin(user_id=message.from_user.id, session=session)
    
    await message.answer(text=html.bold(_("Привет!")))
    