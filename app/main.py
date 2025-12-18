from fastapi import FastAPI

from app.routers import problems

app = FastAPI(title="LeetCode Tracker")

app.include_router(problems.router)


@app.get("/")
async def root():
    return {"status": "System Online"}
