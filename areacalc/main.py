from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

#userdefined function
def calculate_area(length: float, width: float) -> float:
    return length * width

@app.get("/",response_class=HTMLResponse)
async def show_form(request:Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/calculate", response_class=HTMLResponse)
async def handle_form(request: Request, length: float = Form(...), width: float = Form(...)):
    area = calculate_area(length, width)
    return templates.TemplateResponse("result.html",{
        "request":request,
        "length": length,
        "width": width,
        "area": area
    })