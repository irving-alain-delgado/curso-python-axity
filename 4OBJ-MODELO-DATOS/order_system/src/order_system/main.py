from order_system.entities import Order
from order_system.schemas import OrderIn, OrderOut
from pydantic import ValidationError


def main() -> None:
    print("=== CREACIÓN DE ÓRDENES ===")

    order1 = Order(id=1, price=100, quantity=2)  # total = 200
    order2 = Order(id=2, price=50, quantity=3)   # total = 150

    print(order1)
    print(order2)

    print("\n=== COMPARACIÓN ===")
    print("order1 > order2 ?", order1 > order2)

    print("\n=== VALIDACIÓN DATACLASS (__post_init__) ===")
    try:
        Order(id=3, price=-10, quantity=1)
    except ValueError as e:
        print("Error capturado:", e)

    print("\n=== VALIDACIÓN PYDANTIC (OrderIn) ===")

    valid_data = {"price": "100", "quantity": 5}
    order_in = OrderIn(**valid_data)
    print("OrderIn válido:", order_in)

    try:
        invalid_data = {"price": -5, "quantity": 2}
        OrderIn(**invalid_data)
    except ValidationError as e:
        print("Error de Pydantic:")
        print(e)

    print("\n=== CONVERSIÓN A ENTIDAD ===")

    order = Order(id=10, price=order_in.price, quantity=order_in.quantity)
    print("Entidad Order:", order)

    print("\n=== SERIALIZACIÓN OrderOut ===")

    order_out = OrderOut(
        id=order.id,
        price=order.price,
        quantity=order.quantity,
        total=order.total,
    )

    print("Como dict:")
    print(order_out.model_dump())

    print("\nComo JSON:")
    print(order_out.model_dump_json())


if __name__ == "__main__":
    main()