#!/usr/bin/python3

# """ State Module for HBNB project """
# from models.base_model import BaseModel


# class State(BaseModel):
#     """State class"""

#     name = ""

# models/state.py
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
