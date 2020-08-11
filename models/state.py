#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models import storage


class State(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    if (type(storage).__name__ == "FileStorage"):
        print("Lista de ciudades") 
    else:
        cities = relationship("City", backref="state", cascade="all, delete")
