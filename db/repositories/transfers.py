from sqlalchemy.orm import Session

from bot.utils.helpful_functions import transfer_limit
from db import repository as repo
from db.repository import BaseRepository
from db.schemas import TransfersTable

class TransfersTableRepository(BaseRepository):
    table = TransfersTable

    async def create_transfer(self, from_user_id: int, to_user_id: int, 
                              chat_id: int, amount: int, session: Session):
        from_user = await repo.UsersTableRepository().get_user(user_id=from_user_id, session=session)
        to_user = await repo.UsersTableRepository().get_user(user_id=to_user_id, session=session)
        chat = await repo.GroupsTableRepository().get_chat(chat_id=chat_id, session=session)

        if from_user and to_user and chat:
            if transfer_limit(level=from_user.transfer_level) >= (from_user.transfer_limit + amount):
                if from_user.balance >= amount:
                    repo.UsersTableRepository().edit(conditions={"user_id": from_user_id}, 
                        edits={
                            "balance": from_user.balance - amount,
                            "transfer_limit": from_user.transfer_limit + amount
                        }, session=session)
                    repo.UsersTableRepository().edit(conditions={"user_id": to_user_id}, 
                        edits={"balance": to_user.balance + amount}, session=session)

                    self.create(params={
                        "user_id": from_user.id,
                        "to_user_id": to_user.id,
                        "chat_id": chat.id,
                        "amount": amount
                    }, session=session)

                    limit = f"{from_user.transfer_limit + amount}/{transfer_limit(level=from_user.transfer_level)}"

                    return {"success": True, 
                        "transfer": limit, 
                        "error": None}
                else:
                    return {"success": False, "error": "Not enough money!"}
            else:
                return {"success": False, "error": "Limit is full"}

