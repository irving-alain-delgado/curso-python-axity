from fastapi import FastAPI

app = FastAPI()


@app.get("/orders")
def health():
    return {"status": "ok"}