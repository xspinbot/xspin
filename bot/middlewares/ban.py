from aiogram import html
from aiogram.utils.i18n import gettext
from aiogram.types import TelegramObject
from aiogram.dispatcher.middlewares.base import BaseMiddleware

from typing import Any, Awaitable, Callable, Dict
from sqlalchemy.orm import Session

from db import repository as repo
from bot.decorators import create_session
from bot.misc import bot

_ = gettext

class UserBannedMiddleware(BaseMiddleware):
    @create_session
    async def __call__(self, handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]], 
                       event: TelegramObject, data: Dict[str, Any], session: Session) -> Any:
        event_data = event.dict()
        user = await repo.UsersTableRepository().get_user(
            user_id = event_data['from_user']['id'], session = session)

        if not user.is_banned:
            return await handler(event, data)
        else:
            await bot.send_message(chat_id=event_data['chat']['id'], 
                                   text=html.bold(_("Вы забанены 🚫")), 
                                   reply_to_message_id=event_data['message_id'])