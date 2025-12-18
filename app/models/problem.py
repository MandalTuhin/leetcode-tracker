from enum import Enum

from pydantic import BaseModel, Field


class Diffiulty(str, Enum):
    EASY = "Easy"
    MEDIUM = "Medium"
    DIFFICULT = "Difficult"  # I am adding "difficult" for now, I may change it later.


class Problem(BaseModel):
    # ge = Greater than or equal tos
    id: int = Field(ge=1, description="The LeetCode problem Number")
    # min_length = Minimum string length
    title: str = Field(min_length=1, max_length=100)

    difficulty: Diffiulty  # Now restricted to the Enum values
    tags: list[str] = []
    solution_cpp: str | None = Field(None, description="The C++ solution Code")
