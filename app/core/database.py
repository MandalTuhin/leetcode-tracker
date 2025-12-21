import os

from dotenv import load_dotenv
from sqlmodel import Session, SQLModel, create_engine

load_dotenv()

# Use the mount point path defined in Railway (/app/data)
# Fallback to local 'database.db' if the environment variable is not set
DATABASE_PATH = os.getenv("DATABASE_URL", "/app/data/database.db")

# Ensure the URL is correctly formatted for SQLite
if not DATABASE_PATH.startswith("sqlite:///"):
    sqlite_url = f"sqlite:///{DATABASE_PATH}"
else:
    sqlite_url = DATABASE_PATH

# connect_args={"check_same_thread": False} is required for SQLite + FastAPI
engine = create_engine(sqlite_url, echo=True, connect_args={"check_same_thread": False})


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
