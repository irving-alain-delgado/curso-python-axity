from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
# DATABASE_URL = "sqlite:///./orders.db"

from orders_service.infrastructure.config import settings

DATABASE_URL = settings.database_url


class Base(DeclarativeBase):
    pass


engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},  # requerido para SQLite
)

SessionLocal = sessionmaker(bind=engine)