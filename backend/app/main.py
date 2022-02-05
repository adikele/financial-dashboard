from fastapi import FastAPI
from app.api.routers import items, users, assets 
from app.core.config import settings


tags_metadata = [
    {
        "name": "users",
        "description": "Operations with users"
    },
    {
        "name": "items",
        "description": "Operations with items"
    },
    {
        "name": "assets",
        "description": "Operations with assets"
    },
    {
        "name": "admin",
        "description": "Admin operations"
    },
    {
        "name": "auth",
        "description": "Authenticate operations"
    },

]

app = FastAPI(
    title=settings.APP_NAME,
    description="This project provides a base for an asset management site. The projects builds on the base provided by https://github.com/thalesbruno/fastapi-boilerplate",
    version="0.0.1",
    openapi_tags=tags_metadata
)


app.include_router(items.router)
app.include_router(users.router)
app.include_router(assets.router)
