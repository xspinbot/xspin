from sqlalchemy.orm import relationship, mapped_column, Mapped
from sqlalchemy import ForeignKey

from db.config import BaseModel


class GamesHistoryTable(BaseModel):
    __tablename__ = 'games_gamehistory'
    
    user_id: Mapped[int] = mapped_column(ForeignKey('users_user.id'))
    chat_id: Mapped[int] = mapped_column(ForeignKey('groups_group.id'))
    game: Mapped[str] = mapped_column()
    bid: Mapped[int] = mapped_column()
    is_won: Mapped[bool] = mapped_column()

    user: Mapped["UsersTable"] = relationship(back_populates="game_histories")
    chat: Mapped["GroupsTable"] = relationship(back_populates="game_histories")
