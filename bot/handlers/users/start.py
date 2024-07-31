from aiogram import types, html
from aiogram.filters import CommandStart
from aiogram.utils.i18n import gettext

from bot.routers import users_commands as router
from bot.decorators import create_session
from bot.keyboards.inline import start
from bot.texts import texts as txt
from bot.filters import Chat

from db.config import Session
from db import repository as repo

from general.choices import AdminType

_ = gettext

@router.message(Chat().is_private(), CommandStart())
@create_session
async def start_handler(message: types.Message, session: Session):
    admin = await repo.AdminsTableRepository().get_admin(user_id=message.from_user.id, session=session)
    text = message.text

    if len(text.split()) == 2:
        await message.answer(html.bold(_("Referall")))

    await message.answer(text=txt.START(_),
        reply_markup = ((await start.button(True) if admin.level == AdminType.ceo or 
            admin.level == AdminType.admin else await start.button()) if admin else await start.button()
        )
    )