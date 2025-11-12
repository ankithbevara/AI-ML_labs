from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def show_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/submit", response_class=HTMLResponse)
async def handle_form(request: Request, name: str = Form(...), topic: str = Form(...)):
    return templates.TemplateResponse("result.html",{
        "request": request,
        "name": name,
        "topic": topic
    })