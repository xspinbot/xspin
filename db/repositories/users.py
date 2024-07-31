from sqlalchemy.orm import Session
from sqlalchemy import desc, select

from db.repository import BaseRepository
from db.schemas import UsersTable, AdminsTable
from db import repository as repo


class UsersTableRepository(BaseRepository):
    table = UsersTable

    async def get_user(self, user_id: int, session: Session) -> UsersTable:
        with session:
            user = self.get(attribute="user_id", value=user_id, session=session)

            return user

    async def create_user(self, user_id: int, username: str, name: str, 
                        session: Session, update: bool = False):
        with session:
            user = await self.get_user(user_id=user_id, session=session)
            if not user:
                self.create(params={
                    "user_id": user_id,
                    "username": username,
                    "name": name
                }, session=session)
            else:
                if update:
                    self.edit(conditions={
                        "user_id": user_id
                    }, edits={
                        "username": username,
                        "name": name
                    }, session=session)

    async def get_balance(self, user_id: int, session: Session) -> int:
        with session:
            user = await self.get_user(user_id=user_id, session=session)
            if user:
                return user.balance
            else:
                return None
            
    async def update_balance(self, user_id: int, balance: int, session: Session):
        with session:
            return self.edit(conditions={
                "user_id": user_id
            }, edits={
                "balance": balance
            }, session=session)
    
    async def get_top_rating(self, session: Session):
        with session:
            users = (session.execute(
                select(
                    UsersTable.user_id, UsersTable.name, UsersTable.balance
                ).order_by(desc(self.table.balance))
            )).mappings().all()
           
            return users


class AdminsTableRepository(BaseRepository):
    table = AdminsTable

    async def get_admin(self, user_id: int, session: Session) -> AdminsTable:
        user = await repo.UsersTableRepository().get_user(user_id=user_id, session=session)

        if user:
            admin: AdminsTable = self.get(attribute="user_id", value=user.id, session=session)
        else: admin = None
        
        return admin