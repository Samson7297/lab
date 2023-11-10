from pydantic import BaseModel
from typing import Optional
from datetime import date

class BaseEvent(BaseModel):
    title: str
    description: str
    type: str

class Event(BaseEvent):
    id: int
    phone: str
    date: date
    audience: int