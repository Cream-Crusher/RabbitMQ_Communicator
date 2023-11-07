from routes import message_route

from fastapi import FastAPI

app = FastAPI()

app.include_router(message_route.router)
