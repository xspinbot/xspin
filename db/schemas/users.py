from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import ForeignKey

from db.config import BaseModel
from general.choices import LanguageType


class UsersTable(BaseModel):
    __tablename__ = 'users_user'

    user_id: Mapped[int] = mapped_column(unique=True)
    username: Mapped[str] = mapped_column(unique=True)
    language: Mapped[str] = mapped_column(default=LanguageType.ru)
    name: Mapped[str] = mapped_column(nullable=True)
    balance: Mapped[int] = mapped_column(default=10000)
    transfer_limit: Mapped[int] = mapped_column(default=0)
    transfer_level: Mapped[int] = mapped_column(default=1)
    is_banned: Mapped[bool] = mapped_column(default=False)
    
    game_histories: Mapped[list["GamesHistoryTable"]] = relationship(back_populates="user")
    admins: Mapped[list["AdminsTable"]] = relationship(back_populates="user")
    used_promocodes: Mapped[list["UsedPromocodesTable"]] = relationship(back_populates="user")

    user_transfers: Mapped[list["TransfersTable"]] = relationship(
        foreign_keys="[TransfersTable.user_id]", back_populates="user")
    to_user_transfers: Mapped[list["TransfersTable"]] = relationship(
        foreign_keys="[TransfersTable.to_user_id]", back_populates="to_user")

    user_referalls: Mapped[list["ReferallsTable"]] = relationship(
        foreign_keys="[ReferallsTable.user_id]", back_populates="user")
    from_user_referalls: Mapped[list["ReferallsTable"]] = relationship(
        foreign_keys="[ReferallsTable.from_user_id]", back_populates="from_user")

class AdminsTable(BaseModel):
    __tablename__ = 'users_admin'

    user_id: Mapped[int] = mapped_column(ForeignKey('users_user.id'))
    level: Mapped[str] = mapped_column()

    user: Mapped["UsersTable"] = relationship(back_populates="admins")