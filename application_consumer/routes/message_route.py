from fastapi import APIRouter

from messages_broker import MessageBrokerRabbitMQ as RabbitMQ

router = APIRouter()


@router.get('/Message/', tags=['Message'])
async def get_message():
    routing_key = 'route_default'
    message = await RabbitMQ().get_massege(routing_key)

    if message:
        return {"message": message}
    else:
        return {"message": "No messages available"}
