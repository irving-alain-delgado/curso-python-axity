from fastapi import FastAPI, Depends
from pydantic import BaseModel

from orders_service.application.use_cases.create_order import CreateOrderUseCase
from orders_service.infrastructure.db.database import SessionLocal
from orders_service.infrastructure.db.repository_sqlalchemy import SQLAlchemyOrderRepository
from orders_service.infrastructure.messaging.dummy_publisher import DummyEventPublisher
# from orders_service.infrastructure.db import models
from orders_service.infrastructure.config import settings

# Crear tablas (solo desarrollo)
# Base.metadata.create_all(bind=engine)

# app = FastAPI(title="Orders Service")
app = FastAPI(title=settings.app_name)


# -------- Schemas --------

class CreateOrderRequest(BaseModel):
    user_id: str
    product: str
    quantity: int


class OrderResponse(BaseModel):
    id: str
    status: str


# -------- Dependency Injection --------

def get_use_case():
    session = SessionLocal()
    repo = SQLAlchemyOrderRepository(session)
    publisher = DummyEventPublisher()
    return CreateOrderUseCase(repo, publisher)


# -------- Routes --------

@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/orders", response_model=OrderResponse)
def create_order(
    request: CreateOrderRequest,
    use_case: CreateOrderUseCase = Depends(get_use_case),
):
    order = use_case.execute(
        user_id=request.user_id,
        product=request.product,
        quantity=request.quantity,
    )

    return OrderResponse(
        id=order.id,
        status="CREATED",
    )