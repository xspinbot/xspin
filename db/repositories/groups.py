from sqlalchemy.orm import Session

from db.repository import BaseRepository
from db.schemas import GroupsTable

class GroupsTableRepository(BaseRepository):
    table = GroupsTable

    async def get_chat(self, chat_id: int, session: Session):
        with session:
            chat: GroupsTable = self.get(attribute="chat_id", value=chat_id, session=session)

            return chat

    async def create_chat(self, chat_id: int, invite_link: str, username: str, name: str, session: Session):
        with session:
            chat = await self.get_chat(chat_id=chat_id, session=session)
            if not chat:
                return self.create(params={
                    "chat_id": chat_id,
                    "invite_link": invite_link,
                    "username": username,
                    "name": name
                }, session=session)
