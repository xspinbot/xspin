from sqlalchemy.orm import Session
from sqlalchemy import select

from db import repository as repo
from db.repository import BaseRepository
from db.schemas import PromocodesTable, UsedPromocodesTable


class PromocodesTableRepository(BaseRepository):
    table = PromocodesTable

    async def get_promocode(self, promocode: str, session: Session):
        promo = (session.execute(
            select(PromocodesTable).where(PromocodesTable.promocode == promocode)
        )).scalar_one_or_none()

        return promo
    
    async def create_promocode(self, promocode: str, cost: int, max_users: int, session: Session):
        self.create(params={
            "promocode": promocode,
            "cost": cost,
            "max_users": max_users
        }, session=session)

        return None
    

class UsedPromocodesTableRepository(BaseRepository):
    table = UsedPromocodesTable

    async def promocode_used_users_by_id(self, promocode_id: str, session: Session):
        used_users = (session.execute(
            select(self.table).where(UsedPromocodesTable.promocode_id == promocode_id)
        )).scalars().all()

        return used_users
    
    async def get_used_promocode_by_user(self, user_id: int, promocode: str, session: Session):
        user = await repo.UsersTableRepository().get_user(user_id=user_id, session=session)
        promo = await repo.PromocodesTableRepository().get_promocode(
            promocode=promocode, session=session)

        used = (session.execute(
            select(self.table).where(
                (UsedPromocodesTable.user_id == user.id) &
                (UsedPromocodesTable.promocode_id == promo.id)
            )
        )).scalar_one_or_none()

        return used

    async def use_promocode(self, user_id: int, promocode: str, session: Session):
        promo: PromocodesTable = await repo.PromocodesTableRepository().get_promocode(
            promocode=promocode, session=session)
        user = await repo.UsersTableRepository().get_user(
                    user_id=user_id, session=session)
        
        if promo and user:
            used_users = await self.promocode_used_users_by_id(
                promocode_id=promo.id, session=session)
            if len(used_users) < promo.max_users:
                used = await repo.UsedPromocodesTableRepository().get_used_promocode_by_user(
                    user_id=user_id, promocode=promocode, session=session)
                if not used:
                    cost = promo.cost
                    self.create(params={
                        "user_id": user.id,
                        "promocode_id": promo.id
                    }, session=session)

                    await repo.UsersTableRepository().update_balance(
                        user_id=user_id, balance=(user.balance + cost), session=session)

                    return {"success": "True", "cost": cost, "error": None}
                else:
                    return {"success": False, "error": "already used"}
            else:
                return {"success": False, "error": "invalid promocode"}
        else:
            return {"success": False, "error": "not found"}