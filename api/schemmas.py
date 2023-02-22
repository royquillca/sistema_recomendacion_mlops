# Python
from typing import Optional, List, Dict
# Pydantic
from pydantic import BaseModel
# FastAPI
from fastapi import FastAPI


class Movie(BaseModel):
    show_id: str
    type: str
    title: str
    director: str
    cast: str
    country: str
    date_added: str
    release_year: int
    rating: str
    duration_int: float
    duration_type: str
    listed_in: str
    description: str

class User(BaseModel):
    userId: int
    score: float

    