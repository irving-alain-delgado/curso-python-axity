from orm_lab.database import Base, engine, SessionLocal
from orm_lab import crud


def main() -> None:
    Base.metadata.create_all(bind=engine)

    with SessionLocal() as session:
        user = crud.create_user(session, "Irving")
        order = crud.create_order(session, user)
        crud.add_item(session, order, "Laptop", 1500.0)
        crud.add_item(session, order, "Mouse", 50.0)

        print(f"Usuario: {user.name}")
        print(f"Orden ID: {order.id}")
        print(f"Items: {[item.product_name for item in order.items]}")


if __name__ == "__main__":
    main()