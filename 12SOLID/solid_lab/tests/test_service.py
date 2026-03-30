import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from solid_lab.service import OrderService
from solid_lab.adapters.memory_repo import MemoryOrderRepository
from solid_lab.adapters.sql_repo import SqlOrderRepository
from solid_lab.adapters.sql_models import Base


def memory_repo_factory():
    return MemoryOrderRepository()


def sql_repo_factory():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    return SqlOrderRepository(session)


@pytest.mark.parametrize("repo_factory", [
    memory_repo_factory,
    sql_repo_factory,
])
def test_lsp_substitution(repo_factory):
    repo = repo_factory()
    service = OrderService(repo)

    order = service.create_order(1, 100)

    assert order.amount == 100
    assert service.get_order(1).amount == 100