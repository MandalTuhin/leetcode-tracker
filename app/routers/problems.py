from fastapi import APIRouter

from app.core.types import unordered_map
from app.models.problem import Difficulty, Problem

router = APIRouter(prefix="/problems", tags=["Problems"])

db: unordered_map[int, Problem] = {}


@router.post("/")
async def add_problem(problem: Problem):
    db[problem.id] = problem
    return {"message": "Problem added!", "count": len(db)}


# @router.get("/")
# async def get_problems() -> unordered_map[int, Problem]:
#     return db


@router.get("/")
async def search_problems(difficulty: Difficulty | None = None):
    """
    Docstring for search_problems

    :param difficulty: Description
    :type difficulty: Difficulty | None

    Search for problems in unordered_map.
    Time: O(N) for filtering
    """
    if not difficulty:
        return list(db.values())

    results = [p for p in db.values() if p.difficulty == difficulty]
    return results
