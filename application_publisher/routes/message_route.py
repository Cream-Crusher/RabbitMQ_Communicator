from fastapi import APIRouter

from messages_broker import MessageBrokerRabbitMQ as RabbitMQ

router = APIRouter()


@router.post('/Message/', tags=['Message'])
async def post_message(routing_key: str, message: str):
    await RabbitMQ().send_message(message, routing_key)

    return {"message": "Message sent"}
