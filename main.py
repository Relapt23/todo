from fastapi import FastAPI, Form, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")
array = []

@app.get('/ToDo',response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(name="text.html", context={"request":request,"todo": array}) 

@app.post('/ToDo',)
def welcome(request: Request, ToDo = Form()):
    array.append(ToDo)
    return templates.TemplateResponse(name="text.html", context={"request":request,"todo": array})
@app.get("/deleteToDo/{index}")
def delete(request: Request, index):
    array.pop(int(index))
    return templates.TemplateResponse(name="text.html", context={"request":request,"todo": array})
