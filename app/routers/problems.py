from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from app.core.database import get_session
from app.core.types import unordered_map
from app.models.problem import Problem, ProblemCreate

router = APIRouter(prefix="/problems", tags=["Problems"])

db: unordered_map[int, Problem] = {}


@router.post("/", response_model=Problem)
async def create_problem(
    problem_data: ProblemCreate, session: Session = Depends(get_session)
):
    # Call model_validate on the Problem CLASS, passing the data instance
    db_problem = Problem.model_validate(problem_data)

    session.add(db_problem)
    session.commit()
    session.refresh(db_problem)
    return db_problem


@router.get("/", response_model=list[Problem])
async def read_problems(session: Session = Depends(get_session)):
    problems = session.exec(select(Problem)).all()
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
