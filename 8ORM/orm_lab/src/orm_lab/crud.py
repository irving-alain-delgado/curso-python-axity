from sqlalchemy.orm import Session
from orm_lab.models import User, Order, OrderItem


def create_user(session: Session, name: str) -> User:
    user = User(name=name)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


def create_order(session: Session, user: User) -> Order:
    order = Order(user_id=user.id)
    session.add(order)
    session.commit()
    session.refresh(order)
    return order


def add_item(session: Session, order: Order, product: str, price: float) -> OrderItem:
    item = OrderItem(order_id=order.id, product_name=product, price=price)
    session.add(item)
    session.commit()
    session.refresh(item)
    return item