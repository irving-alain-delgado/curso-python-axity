from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from orm_lab.database import Base
from orm_lab.models import User


def test_create_user():
    # ✅ Engine SOLO para testing
    engine = create_engine("sqlite:///:memory:")

    # ✅ Crear tablas en memoria
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)

    with Session() as session:
        user = User(name="TestUser")
        session.add(user)
        session.commit()

        assert user.id is not None