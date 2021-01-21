from sqlalchemy.orm import Session
from .. import models, schemas


def get_event_type(db: Session, event_type_id: int):
    return db.query(models.EventType).filter(models.EventType.id == event_type_id).first()

def get_event_types(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.EventType).offset(skip).limit(limit).all()


def create_event_type(db: Session, event_type: schemas.EventTypeIn):
	db_event_type = models.EventType(**event_type.dict())
	db.add(db_event_type)
	db.commit()
	db.refresh(db_event_type)
	return db_event_type

def delete_event_type(db: Session, event_type_id: int):
    return None