from pydantic import BaseModel, Field


class OrderIn(BaseModel):
    price: float = Field(gt=0)
    quantity: int = Field(gt=0)


class OrderOut(BaseModel):
    id: int
    price: float
    quantity: int
    total: float