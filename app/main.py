from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.database import create_db_and_tables
from app.routers import cache, problems


@asynccontextmanager
async def lifespan(app: FastAPI):
    # --- Startup Logic ---
    # This is where we build the cabinet folders
    create_db_and_tables()
    yield

    print("Server is shutting down...")


app = FastAPI(lifespan=lifespan, title="LeetCode Tracker")

app.include_router(problems.router)
app.include_router(cache.router)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/")
async def root():
    return {"status": "System Online"}
