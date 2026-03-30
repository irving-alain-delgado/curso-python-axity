from pydantic import BaseModel, ConfigDict


class OrderCreate(BaseModel):
    amount: float


class OrderOut(BaseModel):
    id: int
    amount: float

    model_config = ConfigDict(from_attributes=True)