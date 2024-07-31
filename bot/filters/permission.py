from aiogram.filters import Filter
from aiogram.types import TelegramObject
from sqlalchemy.orm import Session

from bot.decorators import create_session
from general.choices import AdminType

from db import repository as repo
from db.schemas import AdminsTable


class Permission(Filter):
    USER = "0"
    SUPERVISOR = AdminType.supervisor
    JUNIOR_ADMIN = AdminType.junior_admin
    ADMIN = AdminType.admin
    CEO = AdminType.ceo

    def __init__(self, permission_classes: list):
        self.permission_classes = [self.CEO]
        self.permission_classes.extend(permission_classes)
        
    @create_session
    async def __call__(self, event: TelegramObject, session: Session, *args, **kwargs) -> bool:
        event_data = event.dict()
        user_id = event_data['from_user']['id']

        user = await repo.UsersTableRepository().get_user(
            user_id=user_id, session=session)
        
        admin: AdminsTable = (
            await repo.AdminsTableRepository().get_admin(user_id=user.user_id, session=session)
        ) if user else None

        return (True if self.USER in self.permission_classes else 
                ((True if admin.level in self.permission_classes else False) 
                if admin else False))
    
    