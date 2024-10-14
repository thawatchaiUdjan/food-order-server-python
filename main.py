from fastapi import FastAPI
from routes import user_route
from db import connect_db, disconnect_db

app = FastAPI(on_startup=[connect_db], on_shutdown=[disconnect_db])

app.include_router(user_route.router)