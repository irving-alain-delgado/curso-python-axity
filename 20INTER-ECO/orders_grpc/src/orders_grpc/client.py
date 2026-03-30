import grpc
from . import orders_pb2
from . import orders_pb2_grpc


def run():
    channel = grpc.insecure_channel("localhost:50051")
    stub = orders_pb2_grpc.OrdersServiceStub(channel)

    response = stub.CreateOrder(
        orders_pb2.CreateOrderRequest(
            user_id="user123",
            product="Laptop",
            quantity=1
        )
    )

    print("Order created:", response.order_id)


if __name__ == "__main__":
    run()