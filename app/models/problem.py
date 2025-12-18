from pydantic import BaseModel
from enum import Enum

class Diffiulty(str, Enum):
    EASY = "Easy"
    MEDIUM = "Medium"
    DIFFICULT = "Difficult" # I am adding "difficult" for now, I may change it later.

class Problem(BaseModel):
    id: int
    title: str
    difficulty: Diffiulty # Now restricted to the Enum values
    tags: list[str] = []
    solution_cpp: str | None = None