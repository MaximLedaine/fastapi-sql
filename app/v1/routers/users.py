from fastapi import Depends, FastAPI, HTTPException, APIRouter
from sqlalchemy.orm import Session
from typing import List
from ..dependencies import VerifyToken
from ..database import get_db

from .. import models, schemas
from ..controllers import users as controller
from ..controllers import events as events_controller

router = APIRouter(
    tags=["users"]
)

@router.post("/users/", response_model=schemas.UserOut)
def create_user(user: schemas.UserIn, db: Session = Depends(get_db)):
    db_user = controller.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return controller.create_user(db=db, user=user)


@router.get("/users/", dependencies=[Depends(VerifyToken())], response_model=List[schemas.UserOut])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = controller.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/users/{user_id}", response_model=schemas.UserOut)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = controller.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.get("/users/{user_id}/events", response_model=List[schemas.EventOut])
def read_user_events(user_id: int, db: Session = Depends(get_db)):
    db_user = controller.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_user_events = db_user.events
    return db_user_events

@router.post("/users/{user_id}/events", response_model=None)
def register_user_events(user_id: int, event_id: int, db: Session = Depends(get_db)):
    db_user = controller.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    db_event = events_controller.get_event(db, event_id=event_id)
    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")

    controller.register_attendance(db, user=db_user, event=db_event)

    return None