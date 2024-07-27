from typing import Any, Awaitable, Callable, Dict
from aiogram.dispatcher.middlewares.base import BaseMiddleware
from aiogram.types import TelegramObject
from aiogram.enums import ChatType
from sqlalchemy.orm import Session

from db import repository as repo
from bot.decorators import create_session
from bot.misc import bot

class CreateUserAndChatMiddleware(BaseMiddleware):
    @create_session
    async def __call__(self, handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]], 
                       event: TelegramObject, data: Dict[str, Any], session: Session) -> Any:
        event_data = event.dict()

        await repo.UsersTableRepository().create_user(
                user_id = event_data['from_user']['id'],
                username = event_data['from_user']['username'],
                name = (event_data['from_user']['first_name'] + 
                        (event_data['from_user']['last_name'] 
                        if event_data['from_user']['last_name'] else "")),
                session = session
            )
        
        if event_data['chat']['type'] in (ChatType.GROUP, ChatType.GROUP):
            chat = await bot.get_chat(chat_id=event_data['chat']['id'])
            await repo.GroupsTableRepository().create_chat(
                chat_id=chat.id,
                invite_link=chat.invite_link,
                username=chat.username,
                name=chat.full_name,
                session=session
            )
        
        return await handler(event, data)
