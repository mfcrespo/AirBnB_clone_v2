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

    if (type(storage).__name__ != "FileStorage"):
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        @property
        def get_cities(self):
            """ getter method for cities"""
            cities_dict = {}
            for key in storage.all(City):
                if self.id in key:
                    cities_dict[key] = storage.all(City)[key]
            return cities_dict
