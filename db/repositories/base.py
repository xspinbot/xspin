from typing import Any

from sqlalchemy.exc import IntegrityError
from sqlalchemy import select, insert, delete, update, and_
from sqlalchemy.orm import Session
from db.config import current_time


class BaseRepository:
    table = None

    @classmethod
    def get(cls, attribute: str, value: Any, session: Session):
        with session:
            instance = (session.execute(
                select(cls.table).where(getattr(cls.table, attribute) == value)
            )).scalar()

        return instance

    @classmethod
    def get_many(cls, attribute: str, value: Any, session: Session):
        with session:
            instances = (session.execute(
                select(cls.table).where(getattr(cls.table, attribute) == value)
            )).scalars()

        return instances

    @classmethod
    def is_exist(cls, attribute: str, value: Any, session: Session):
        with session:
            instance = (session.execute(
                select(getattr(cls.table, attribute)).where(
                    getattr(cls.table, attribute) == value))).scalar()

            return bool(instance)

    @classmethod
    def edit(cls, conditions: dict, edits: dict, session: Session):
        edits['updated_at'] = current_time().utcnow()
        with session:
            where_condition = and_(*[getattr(cls.table, field) == value for field, value in conditions.items()])
            stmt = update(cls.table).where(where_condition).values(**edits)
            session.execute(stmt)
            session.commit()
        return None

    @classmethod
    def create(cls, params: dict, session: Session):
        with session:
            instance = cls.table(**params)

            session.add(instance)
            session.commit()
            session.refresh(instance)
        return instance

    @classmethod
    def delete(cls, conditions: dict, session):
        try:
            where_condition = and_(*[getattr(cls.table, field) == value for field, value in conditions.items()])
        except AttributeError:
            return None
        with session:
            stmt = delete(cls.table).where(where_condition)
            session.execute(stmt)
            session.commit()

    @classmethod
    def get_or_create(cls, conditions: dict, params: dict, session: Session):
        try:
            result = cls.create(params=params, session=session)
            return result, True
        except IntegrityError:
            with session:
                where_condition = and_(*[getattr(cls.table, field) == value for field, value in conditions.items()])
                result = session.query(cls.table).filter(where_condition).scalar()
                return result, False

    @classmethod
    def get_and_update(cls, conditions: dict, edits: dict, session: Session):
        with session:
            where_condition = and_(*[getattr(cls.table, field) == value for field, value in conditions.items()])
            try:
                instance = (session.execute(select(cls.table).where(where_condition))).scalar()
                for key, value in edits.items():
                    setattr(instance, key, value)
                session.add(instance)
                session.commit()
            except:
                return None
            return instance