from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Todo(BaseModel):
    
    title: str
    description: str
    completed: bool
next_id=1
todos = []


@app.get("/")
def home():
    return {"message": "Todo API Running"}

@app.post("/todo")

def new_todo(todo:Todo):
    global next_id
    tododict=todo.model_dump()
    tododict['id']=next_id
    todos.append(tododict)
    next_id+=1
    return {
        "message": 'done',
        'todo' : tododict
    }
    
@app.get("/todos")
def get_todos():
    return {"todos": todos}
@app.get("/todo/{n}")
def get_particular_todo(n:int):
    return todos[n]
@app.delete("/todo/{n}")
def del_todo(n: int):
    removed = todos.pop(n)
    return {
        "deleted": removed
    }

@app.put("/todo/{n}")
def update_todo(n: int,todo: Todo):
    old_id = todos[n]["id"]
    updated = todo.model_dump()
    updated["id"] = old_id
    todos[n] = updated

@app.get("/completed")

def completed_tasks():
    completed1=[]
    for todo in todos:
      if(todo["completed"]==True):
         completed1.append(todo)

    return completed1    
         
@app.get("/stats")

def stats():
    k=dict([])
    l=[]
    for todo in todos:
      if(todo["completed"]==True):
         l.append(todo)
    k["total_ids"]=len(todos)
    k["completed"]=len(l)
    return k
