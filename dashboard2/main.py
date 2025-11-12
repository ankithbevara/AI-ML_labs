from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

@app.post("/submit", response_class=HTMLResponse)
async def submit_form(
    request: Request,
    name: str = Form(...),
    role: str = Form(...),
    topic: str = Form(...),
    delivery_mode: str = Form(...)
):
    return templates.TemplateResponse("result.html",{
        "request": request,
        "name": name,
        "role": role,
        "topic": topic,
        "delivery_mode": delivery_mode
    })
