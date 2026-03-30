import os
import typer
import httpx

app = typer.Typer()

API_URL = os.getenv("API_URL", "http://localhost:8000")


@app.command()
def list():
    """List all orders"""
    response = httpx.get(f"{API_URL}/orders")
    response.raise_for_status()
    typer.echo(response.json())


@app.command()
def create(amount: float):
    """Create a new order"""
    response = httpx.post(
        f"{API_URL}/orders",
        json={"amount": amount},
    )
    response.raise_for_status()
    typer.echo(response.json())


@app.command()
def delete(order_id: int):
    """Delete an order"""
    response = httpx.delete(f"{API_URL}/orders/{order_id}")
    response.raise_for_status()
    typer.echo("Order deleted")
