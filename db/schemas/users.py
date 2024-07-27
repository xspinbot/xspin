from db.config import BaseModel
from general.choices import LanguageType
from sqlalchemy.orm import relationship, Mapped, mapped_column

class UsersTable(BaseModel):
    __tablename__ = 'users_user'

    user_id: Mapped[int] = mapped_column(unique=True)
    username: Mapped[str] = mapped_column(unique=True)
    language: Mapped[str] = mapped_column(default=LanguageType.ru)
    name: Mapped[str] = mapped_column(nullable=True)
    balance: Mapped[int] = mapped_column(default=0)
    transfer_limit: Mapped[int] = mapped_column(default=0)
    transfer_level: Mapped[int] = mapped_column(default=0)
    is_banned: Mapped[bool] = mapped_column(default=False)
    
    game_histories: Mapped[list["GamesHistoryTable"]] = relationship(back_populates="user")