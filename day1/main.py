from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

#setting up the template directory
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_home(request: Request):
    #pass dynamic data to the template
    return templates.TemplateResponse("home.html", {
        "request": request,
        "title": "Welcome to FastAPI",
        "username": "Ankith",
        "topics": ["FastAPI", "Jinja2", "HTML Rendering", "Curriculum Design"]
    })


# unicorn main:app --port 8000 --reload, so when you run this in terminal by default it runs every time in port 8000