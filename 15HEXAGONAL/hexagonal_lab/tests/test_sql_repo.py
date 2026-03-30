from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from hexagonal_lab.infrastructure.sql_models import Base
from hexagonal_lab.infrastructure.sql_repo import SqlOrderRepository
from hexagonal_lab.domain.order import Order


def test_sql_repository():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)

    with Session() as session:
        repo = SqlOrderRepository(session)

        order = Order(id=1, amount=100)
        repo.save(order)

        retrieved = repo.get(1)

        assert retrieved == order