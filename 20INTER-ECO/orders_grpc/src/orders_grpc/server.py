import grpc
from concurrent import futures
import uuid
import json
import pika

from orders_grpc import orders_pb2
from orders_grpc import orders_pb2_grpc


class OrdersService(orders_pb2_grpc.OrdersServiceServicer):

    def CreateOrder(self, request, context):
        order_id = str(uuid.uuid4())

        # Publicar evento en RabbitMQ
        publish_event({
            "event": "OrderCreated",
            "order_id": order_id,
            "user_id": request.user_id,
            "product": request.product,
            "quantity": request.quantity
        })

        return orders_pb2.OrderResponse(
            order_id=order_id,
            status="CREATED"
        )


def publish_event(event_data):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters("localhost")
    )
    channel = connection.channel()

    channel.queue_declare(queue="orders")

    channel.basic_publish(
        exchange="",
        routing_key="orders",
        body=json.dumps(event_data)
    )

    connection.close()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    orders_pb2_grpc.add_OrdersServiceServicer_to_server(
        OrdersService(), server
    )

    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()