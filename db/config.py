import datetime
import pytz

from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import (declarative_base, DeclarativeBase,
                            Session, sessionmaker,
                            Mapped, mapped_column)

from data.config import PostgresSettings


psql = PostgresSettings()

engine: Engine = create_engine(
    PostgresSettings().url
)

SessionLocal: Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base: DeclarativeBase = declarative_base()

tashkent_tz = pytz.timezone('Asia/Tashkent')

def current_time(time_zone=True):
    if time_zone:
        return datetime.datetime.now(tz=tashkent_tz)
    else:
        return datetime.datetime.now()

class BaseModel(Base):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    created_at: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.utcnow)
    updated_at: Mapped[datetime.datetime] = mapped_column(onupdate=datetime.datetime.utcnow)
    is_active: Mapped[bool] = mapped_column(default=True)

    @property
    def created_at_utc(self) -> datetime.datetime:
        if self.created_at:
            return self.created_at + datetime.timedelta(hours=5)

    @property
    def updated_at_utc(self) -> datetime.datetime:
        if self.updated_at:
            return self.updated_at + datetime.timedelta(hours=5)


