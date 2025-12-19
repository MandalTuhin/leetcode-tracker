from enum import Enum

from sqlmodel import Field, SQLModel


class Difficulty(str, Enum):
    EASY = "Easy"
    MEDIUM = "Medium"
    DIFFICULT = "Difficult"  # I am adding "difficult" for now, I may change it later.


class ProblemBase(SQLModel):
    problem_no: int = Field(unique=True, index=True)
    title: str = Field(index=True)
    difficulty: Difficulty
    solution_cpp: str | None = None


class ProblemCreate(ProblemBase):
    pass


class Problem(ProblemBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
