from typing import Annotated
from fastapi import FastAPI, Form
from pydantic import BaseModel
from enum import Enum

# Define pydantic models
class Category1(str, Enum):
    option1 = "option1"
    option2 = "option2"
    option3 = "option3"

# Create api models
class ApiForm(BaseModel):
    category: Category1
    string1: str
    strin2: str
    number1: int
    number2: float
