from aiogram import types, html
from aiogram.filters import Command
from aiogram.utils.i18n import gettext

from bot.routers import users_commands as router
from bot.decorators import create_session
from bot.keyboards.inline import start
from bot.texts import texts as txt
from bot.filters import Chat
from bot.misc import bot_settings

from db.config import Session
from db import repository as repo

from general.choices import AdminType

_ = gettext

@router.message(Chat().is_private(), Command("referall"))
@create_session
async def referall_handler(message: types.Message, session: Session):
    admin = await repo.UsersTableRepository().get_user(user_id=message.from_user.id, 
                                                       session=session)
    
    await message.answer(text=(html.bold(_("🔗 Ваша реферальная ссылка: ")) + 
        "\n\n" + html.code(f"https://t.me/{bot_settings.name}?start={message.from_user.id}")))