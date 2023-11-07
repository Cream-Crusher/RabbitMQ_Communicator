from fastapi import APIRouter

from message_broker import get_massege

router = APIRouter()


@router.get('/Message/', tags=['Message'])
async def get_message():
    routing_key = 'route_default'
    message = await get_massege(routing_key)

    if message:
        body = message.body.decode()
        return {"message": body}
    else:
        return {"message": "No messages available"}
