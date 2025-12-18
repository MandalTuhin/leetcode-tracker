from enum import Enum

from sqlmodel import Field, SQLModel


class Difficulty(str, Enum):
    EASY = "Easy"
    MEDIUM = "Medium"
    DIFFICULT = "Difficult"  # I am adding "difficult" for now, I may change it later.


class Problem(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(index=True)  # index=True makes searches O(log n)
    difficulty: Difficulty  # restricted to the Enum values
    # tags: list[str] = []
    solution_cpp: str | None = None
