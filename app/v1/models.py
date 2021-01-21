from sqlalchemy import Boolean, Table, Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship

from .database import Base

user_event = Table('user_event', Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id')),
    Column('event_id', Integer, ForeignKey('event.id'))
)

user_membership_transaction = Table('user_membership_transaction', Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id')),
    Column('membership_id', Integer, ForeignKey('membership.id')),
    Column('transaction_id', Integer, ForeignKey('transaction.id'))
)

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    is_active = Column(Boolean, default=True)
    events = relationship("Event", secondary=user_event, back_populates="attendees")
    memberships = relationship("user_membership_transaction", secondary=user_membership_transaction)


class Event(Base):
    __tablename__ = "event"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    date = Column(DateTime)
    location = Column(String)
    image= Column(String)
    url= Column(String)
    type= Column(String)
    tags= Column(String)
    event_type_id = Column(Integer, ForeignKey('event_type.id'))
    event_type = relationship("EventType")
    attendees = relationship("User", secondary=user_event, back_populates="events")

class EventType(Base):
    __tablename__ = "event_type"

    id = Column(Integer, primary_key=True)
    name = Column(String)

class Transaction(Base):
    __tablename__ = "transaction"

    id = Column(Integer, primary_key=True)
    name = Column(String)

class Membership(Base):
    __tablename__ = "membership"

    id = Column(Integer, primary_key=True)
    name = Column(String)