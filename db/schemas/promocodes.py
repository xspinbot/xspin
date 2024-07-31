from db.config import BaseModel
from sqlalchemy.orm import relationship, mapped_column, Mapped
from sqlalchemy import ForeignKey


class PromocodesTable(BaseModel):
    __tablename__ = 'promocodes_promocode'

    promocode: Mapped[str] = mapped_column(unique=True)
    cost: Mapped[int] = mapped_column()
    max_users: Mapped[int] = mapped_column()

    used_promocodes: Mapped[list["UsedPromocodesTable"]] = relationship(back_populates="promocode")

class UsedPromocodesTable(BaseModel):
    __tablename__ = 'promocodes_usedpromocode'

    user_id: Mapped[int] = mapped_column(ForeignKey("users_user.id"))
    promocode_id: Mapped[int] = mapped_column(ForeignKey("promocodes_promocode.id"))

    user: Mapped["UsersTable"] = relationship(back_populates="used_promocodes")
    promocode: Mapped["PromocodesTable"] = relationship(back_populates="used_promocodes")
