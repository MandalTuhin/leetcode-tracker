from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session, select

from app.core.database import get_session
from app.models.problem import Problem, ProblemCreate, ProblemUpdate

router = APIRouter(prefix="/problems", tags=["Problems"])


@router.post("/", response_model=Problem, status_code=status.HTTP_201_CREATED)
async def create_problem(
    problem_data: ProblemCreate, session: Session = Depends(get_session)
):
    dB_problem = Problem.model_validate(problem_data)

    try:
        session.add(dB_problem)
        session.commit()
        session.refresh(dB_problem)
    except IntegrityError:
        session.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Problem number {problem_data.problem_no} already exists.",
        )
    return dB_problem


@router.get("/", response_model=list[Problem])
async def read_problems(session: Session = Depends(get_session)):
    problems = session.exec(select(Problem)).all()
    return problems


@router.get("/{problem_id}", response_model=Problem)
async def read_problem(problem_id: int, session: Session = Depends(get_session)):
    """
    Fetch a single LeetCode problem by its internal database ID.
    """

    # session.get() is the most efficient way to find a row by its primary key.
    problem = session.get(Problem, problem_id)

    if not problem:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Problem with ID {problem_id} not found",
        )

    return problem


@router.patch("/{problem_id}", response_model=Problem)
async def update_problem(
    problem_id: int,
    problem_update: ProblemUpdate,
    session: Session = Depends(get_session),
):
    dB_problem = session.get(Problem, problem_id)
    if not dB_problem:
        raise HTTPException(
            status_code=404, detail=f"Problem ID {problem_id} not found."
        )

    update_data = problem_update.model_dump(exclude_unset=True)

    # Update only the provided fields
    dB_problem.sqlmodel_update(update_data)

    session.add(dB_problem)
    session.commit()
    session.refresh(dB_problem)
    return dB_problem


@router.delete("/{problem_id}")
async def delete_problem(problem_id: int, session: Session = Depends(get_session)):
    dB_problem = session.get(Problem, problem_id)

    if not dB_problem:
        raise HTTPException(
            status_code=404, detail=f"Problem with ID {problem_id} not found"
        )
    session.delete(dB_problem)
    session.commit()
    return {"ok": True}


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
