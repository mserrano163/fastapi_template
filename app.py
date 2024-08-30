# Import libraries and plugins
import logging 
import os
from fastapi import FastAPI
from pydantic import BaseModel
from pathlib import Path
from enum import Enum
from dotenv import load_dotenv

from plugins import (
    ApiForm,
    success_response
)


# Get Environment variables
BASE_DIR = Path(__file__).resolve().parent
ENV_FILE_PATH = BASE_DIR / ".env"
load_dotenv(ENV_FILE_PATH)

# Initialize FastAPI
your_app_name = FastAPI()

# Setup basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# API methods
@your_app_name.get("/hello_world")
def your_app_hello():
    return success_response("Hello World")