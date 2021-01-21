from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel

class UserIn(BaseModel):
    email: str
    is_active: bool

    class Config:
        orm_mode = True

class UserOut(BaseModel):
    id: int
    email: str
    is_active: bool

    class Config:
        orm_mode = True

class EventTypeIn(BaseModel):
    name: str

    class Config:
        orm_mode = True

class EventTypeOut(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class EventIn(BaseModel):
    name: str
    description: str
    date: datetime
    location: str
    image: str
    url: str
    type: str
    tags: str
    event_type_id: int

    class Config:
        orm_mode = True

class EventOut(BaseModel):
    id: int
    name: str
    description: str
    date: datetime
    location: str
    image: str
    url: str
    type: str
    tags: str
    event_type: EventTypeOut

    class Config:
        orm_mode = True