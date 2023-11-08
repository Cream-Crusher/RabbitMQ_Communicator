from fastapi import APIRouter

from messages_broker import MessageBrokerRabbitMQ as RabbitMQ

router = APIRouter()


@router.get('/Message/', tags=['Message'])
async def get_message():
    routing_key = 'route_default'
    message = await RabbitMQ().get_massege(routing_key)

    if message:
        body = message.body.decode()
        return {"message": body}
    else:
        return {"message": "No messages available"}
