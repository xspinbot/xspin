import functools
from contextlib import asynccontextmanager

from db.config import SessionLocal, Session
from sqlalchemy.ext.asyncio import AsyncSession


@asynccontextmanager
async def session_scope():
    session: Session = SessionLocal()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def create_session(func):
    @functools.wraps(func)
    async def inner(*args, **kwargs):
        if not kwargs.get("session"):
            async with session_scope() as session:
                kwargs["session"] = session
                return await func(*args, **kwargs)
        else:
            return await func(*args, **kwargs)
    return inner
