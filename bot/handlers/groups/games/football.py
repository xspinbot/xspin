from aiogram import types
from aiogram import enums
from aiogram.enums import DiceEmoji
from sqlalchemy.orm import Session

from bot.routers import games as router
from bot.filters import Text, Chat, ContentType
from bot.utils.helpful_functions import Play
from bot.decorators import create_session


@router.message(Chat().is_group(), ContentType(enums.ContentType.TEXT), Text(startswith='!ф '))
@create_session
async def football_handler(message: types.Message, session: Session):
    await Play().play(
        message=message,
        game=DiceEmoji.FOOTBALL,
        session=session
    )