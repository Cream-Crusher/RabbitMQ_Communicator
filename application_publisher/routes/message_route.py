from fastapi import APIRouter

from message_broker import send_message

router = APIRouter()


@router.post('/Message/', tags=['Message'])
async def post_message(message: str):
    routing_key = 'route_default'
    await send_message(message, routing_key)

    return {"message": "Message sent"}
