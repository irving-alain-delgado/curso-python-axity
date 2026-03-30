import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fastapi_lab.database import Base
from fastapi_lab.main import app
from fastapi_lab.dependencies import get_db


@pytest.fixture
def test_client():
    engine = create_engine("sqlite:///:memory:")
    TestingSessionLocal = sessionmaker(bind=engine)

    Base.metadata.create_all(bind=engine)

    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db

    from fastapi.testclient import TestClient
    return TestClient(app)