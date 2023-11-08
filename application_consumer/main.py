from fastapi import FastAPI

from routes import message_route

app = FastAPI()

app.include_router(message_route.router)
