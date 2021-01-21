from typing import List

from fastapi import Depends, FastAPI, HTTPException, APIRouter

from .database import SessionLocal, engine

from . import models

from .routers import users, events, event_types

models.Base.metadata.create_all(bind=engine)

router = APIRouter()
router.include_router(users.router)
router.include_router(events.router)
router.include_router(event_types.router)

