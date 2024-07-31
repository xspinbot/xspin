from db.repository import BaseRepository
from db.schemas import GamesHistoryTable
from db import repository as repo
from sqlalchemy.orm import Session

class GamesHistoryTableRepository(BaseRepository):
    table = GamesHistoryTable

    async def create_game(self, user_id: int, chat_id: int, 
                          game: str, bid: int, is_won: 
                          bool, session: Session):
        user = await repo.UsersTableRepository().get_user(user_id=user_id, session=session)
        chat = await repo.GroupsTableRepository().get_chat(chat_id=chat_id, session=session)

        if user and chat:
            return self.create(params={
                "user": user,
                "chat": chat,
                "game": game,
                "bid": bid,
                "is_won": is_won
            }, session=session)