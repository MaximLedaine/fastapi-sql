from sqlalchemy.orm import Session
from fastapi import APIRouter
from typing import List
from fastapi import Depends, FastAPI, HTTPException
from .. import models, schemas
from ..controllers import event_types as controller
from ..database import get_db

router = APIRouter(
    tags=["event_types"]
)

@router.post("/event_types/", response_model=schemas.EventTypeOut)
def create_event_type(event_type: schemas.EventTypeIn, db: Session = Depends(get_db)):
    return controller.create_event_type(db=db, event_type=event_type)


@router.get("/event_types/", response_model=List[schemas.EventTypeOut])
def read_event_types(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    event_types = controller.get_event_types(db, skip=skip, limit=limit)
    return event_types


@router.get("/event_types/{event_id}", response_model=schemas.EventTypeOut)
def read_event_type(event_type_id: int, db: Session = Depends(get_db)):
    db_event_type = controller.get_event_type(db, event_type_id=event_type_id)
    if db_event_type is None:
    	raise HTTPException(status_code=404, detail="Event not found")
    return db_event_type
