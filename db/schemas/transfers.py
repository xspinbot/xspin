from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import ForeignKey
from db.config import BaseModel


class TransfersTable(BaseModel):
    __tablename__ = "transfers_transfer"

    user_id: Mapped[int] = mapped_column(ForeignKey('users_user.id'))
    to_user_id: Mapped[int] = mapped_column(ForeignKey('users_user.id'))
    chat_id: Mapped[int] = mapped_column(ForeignKey('groups_group.id'))
    amount: Mapped[int] = mapped_column()

    user: Mapped["UsersTable"] = relationship(foreign_keys=[user_id], 
                                              back_populates="user_transfers")
    to_user: Mapped["UsersTable"] = relationship(foreign_keys=[to_user_id],
                                                 back_populates="to_user_transfers")
    chat: Mapped["GroupsTable"] = relationship(back_populates="transfers")
