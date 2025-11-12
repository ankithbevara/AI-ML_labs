from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

def calculate_area(length: float, width: float) -> float:
    return length * width

class Rectangle(BaseModel):
    length: float
    width: float


@app.post("/area")
def get_area(rect: Rectangle):
    area = calculate_area(rect.length, rect.width)
    return{
        "length": rect.length,
        "width": rect.width,
        "area": area
    }