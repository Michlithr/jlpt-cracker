from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlmodel import SQLModel

from .database import engine
from .routers import ALL_ROUTERS


async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Creating tables...")
    await create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)

for router in ALL_ROUTERS:
    app.include_router(router)
