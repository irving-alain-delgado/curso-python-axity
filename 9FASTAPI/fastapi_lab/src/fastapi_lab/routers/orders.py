from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from fastapi_lab.schemas import OrderCreate, OrderOut
from fastapi_lab.models import Order
from fastapi_lab.dependencies import get_db, get_current_user

router = APIRouter(prefix="/orders", tags=["orders"])


# ✅ CREATE
@router.post(
    "/",
    response_model=OrderOut,
    status_code=status.HTTP_201_CREATED,
)
def create_order(
    order: OrderCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    db_order = Order(amount=order.amount, user_id=1)  # simplificado
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


# ✅ READ ALL
@router.get(
    "/",
    response_model=List[OrderOut],
)
def get_orders(
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    return db.query(Order).all()


# ✅ READ ONE
@router.get(
    "/{order_id}",
    response_model=OrderOut,
)
def get_order(
    order_id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    order = db.query(Order).filter(Order.id == order_id).first()

    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found",
        )

    return order


# ✅ DELETE
@router.delete(
    "/{order_id}",
    status_code=status.HTTP_200_OK,
)
def delete_order(
    order_id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    order = db.query(Order).filter(Order.id == order_id).first()

    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found",
        )

    db.delete(order)
    db.commit()

    return {"message": "Order deleted"}