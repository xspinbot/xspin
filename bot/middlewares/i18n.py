from typing import Any, Dict
from aiogram.fsm.context import FSMContext
from aiogram.utils.i18n import I18nMiddleware as BaseI18nMiddleware
from aiogram.types import TelegramObject, Update
from sqlalchemy.orm import Session
from aiogram import Bot

from db import repository as repo
from bot.decorators import create_session


class I18nMiddleware(BaseI18nMiddleware):
    @create_session
    async def get_locale(self, event: TelegramObject, data: Dict[str, Any], session: Session) -> str:
        event_dict = event.dict()
        if 'from_user' in event_dict:
            user_id = event_dict['from_user']['id']
            user = await repo.UsersTableRepository().get_user(user_id=user_id, session=session)
            
            if user and user.language:
                return user.language
            else:
                return 'ru'
        else:
            return 'ru'
