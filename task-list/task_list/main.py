from task import Task
from fastapi import FastAPI

app =  FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/tasks")
async def read_tasks():
    return {"tasks": [{}, {}]}

@app.get("/tasks/{task_id}")
async def read_task(task_id: int):
    return {}