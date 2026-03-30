from fastapi import FastAPI
from fastapi_lab.database import Base, engine
from fastapi_lab.routers import orders, auth

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(orders.router)