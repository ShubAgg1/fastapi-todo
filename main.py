from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello World"}
@app.get("/hello")
def hello():
    return {"msg": "Hi"}
@app.get("/square/{n}")
def square(n: int):
    return {"answer": n * n}
@app.get("/add/{a}/{b}")
def add(a:int,b:int):
    return {"answer": a+b}
@app.get("/max/{a}/{b}")
def max(a:int,b:int):
    m=0
    if(a>b):
        m=a
    else:
        m=b    
    return {"answer": m}
@app.get("/search")
def search(q: str):
    return {"query": q}

class Todo(BaseModel):
    title: str
    completed: bool

@app.post("/todo")
def create_todo(todo: Todo):
    return {
        "message": "Todo created",
        "todo": todo
    }