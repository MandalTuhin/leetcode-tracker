from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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

origins = [
    "http://localhost:5173",  # Standard Vite/SvelteKit dev port
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows specific origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, PATCH, etc.)
    allow_headers=["*"],  # Allows all headers
)

app.include_router(problems.router)
app.include_router(cache.router)


@app.get("/")
async def root():
    return {"status": "System Online"}
