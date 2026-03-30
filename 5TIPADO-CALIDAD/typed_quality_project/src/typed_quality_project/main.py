from typed_quality_project.models import Order


def main() -> None:
    order = Order(id=1, amount=100.0, status="pending")

    order.pay()

    data = order.to_dict()

    print(order)
    print(data)


if __name__ == "__main__":
    main()
