from fastapi import FastAPI
from .settings import settings

app = FastAPI(title=settings.app_name)


@app.get("/docs")
def read_root():
    return {
        "app": settings.app_name,
        "debug": settings.debug,
    }