from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import ForeignKey
from db.config import BaseModel


class ReferallsTable(BaseModel):
    __tablename__ = "referalls_referall"

    user_id: Mapped[int] = mapped_column(ForeignKey('users_user.id'))
    from_user_id: Mapped[int] = mapped_column(ForeignKey('users_user.id'))

    user: Mapped["UsersTable"] = relationship(foreign_keys=[user_id], 
                                              back_populates="user_referalls")
    from_user: Mapped["UsersTable"] = relationship(foreign_keys=[from_user_id],
                                                 back_populates="from_user_referalls")
