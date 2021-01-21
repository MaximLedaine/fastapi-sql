from fastapi import Depends, FastAPI, HTTPException, Security, APIRouter
from sqlalchemy.orm import Session
from typing import List
from ..dependencies import VerifyToken
from ..database import get_db

from .. import models, schemas
from ..controllers import events as controller
from ..controllers import event_types as event_types_controller


router = APIRouter(
    tags=["events"]
)

@router.post("/events/", dependencies=[Depends(VerifyToken())], response_model=schemas.EventOut)
def create_event(event: schemas.EventIn, db: Session = Depends(get_db)):
    db_event_type = event_types_controller.get_event_type(db=db, event_type_id= event.event_type_id)
    if db_event_type is None:
    	raise HTTPException(status_code=404, detail="Event not found")
    return controller.create_event(db=db, event=event)


@router.get("/events/", response_model=List[schemas.EventOut])
def read_events(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    events = controller.get_events(db, skip=skip, limit=limit)
    return events


@router.get("/events/{event_id}", response_model=schemas.EventOut)
def read_event(event_id: int, db: Session = Depends(get_db)):
    db_event = controller.get_event(db, event_id=event_id)
    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return db_event

@router.delete("/events/{event_id}", response_model=schemas.EventOut)
def read_event(event_id: int, db: Session = Depends(get_db)):
    db_event = controller.delete_event(db, event_id=event_id)
    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return db_event
