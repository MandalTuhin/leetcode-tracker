from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from app.core.database import get_session
from app.core.types import unordered_map
from app.models.problem import Problem

router = APIRouter(prefix="/problems", tags=["Problems"])

db: unordered_map[int, Problem] = {}


@router.post("/")
async def create_problem(problem: Problem, session: Session = Depends(get_session)):
    session.add(problem)
    session.commit()
    session.refresh(problem)
    return problem


@router.get("/")
async def read_problems(session: Session = Depends(get_session)):
    problems = session.exec(select(Problem)).all
    return problems


# @router.get("/")
# async def search_problems(difficulty: Difficulty | None = None):
#     """
#     Docstring for search_problems

#     :param difficulty: Description
#     :type difficulty: Difficulty | None

#     Search for problems in unordered_map.
#     Time: O(N) for filtering
#     """
#     if not difficulty:
#         return list(db.values())

#     results = [p for p in db.values() if p.difficulty == difficulty]
#     return results
