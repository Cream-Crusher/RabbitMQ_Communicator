from fastapi import APIRouter

from messages_broker import MessageBrokerRabbitMQ as RabbitMQ

router = APIRouter()


@router.post('/Message/', tags=['Message'])
async def post_message(message: str):
    routing_key = 'route_default'
    await RabbitMQ().send_message(message, routing_key)

    return {"message": "Message sent"}
