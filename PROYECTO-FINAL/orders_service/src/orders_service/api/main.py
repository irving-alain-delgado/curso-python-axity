from fastapi import FastAPI, Depends
from pydantic import BaseModel

from orders_service.application.use_cases.create_order import CreateOrderUseCase
from orders_service.infrastructure.db.database import SessionLocal
from orders_service.infrastructure.db.repository_sqlalchemy import SQLAlchemyOrderRepository
from orders_service.infrastructure.messaging.dummy_publisher import DummyEventPublisher
# from orders_service.infrastructure.db import models
from orders_service.infrastructure.config import settings
from sqlalchemy.orm import Session
from typing import Generator
import logging
from orders_service.domain.exceptions import DomainError
from fastapi import Request
from fastapi.responses import JSONResponse
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


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# -------- Dependency Injection --------

def get_use_case(db: Session = Depends(get_db)):
    repo = SQLAlchemyOrderRepository(db)
    publisher = DummyEventPublisher()
    return CreateOrderUseCase(repo, publisher)


# -------- Exceptions --------

@app.exception_handler(DomainError)
async def domain_exception_handler(request: Request, exc: DomainError):
    return JSONResponse(
        status_code=400,
        content={"detail": str(exc)},
    )



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



logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)

logger = logging.getLogger(__name__)