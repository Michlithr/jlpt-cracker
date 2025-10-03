import os
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel import Session, SQLModel

DATABASE_URL = os.environ.get("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable not set. Check your .env file.")

engine = create_async_engine(DATABASE_URL, echo=True)


async def get_session() -> AsyncGenerator[Session, None]:
    async with Session(engine) as session:
        yield session


# Define a placeholder table creation function (used at startup)
# NOTE: Replace this with Alembic migrations.
async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


# The FastAPI lifespan context handles startup/shutdown logic.
@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    # Startup: Create tables before the app starts serving requests
    print("Creating tables...")
    await create_db_and_tables()
    yield
    # Shutdown: (Optional: Clean up resources)


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def read_root():
    return {
        "status": "ok",
        "message": "Backend running and database connection configured.",
    }
