#!/usr/bin/python3
""" State Module for HBNB project """

from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
import models
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade="all, delete")
    else:
        name = ""

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """"""
            list_cities = []
            cls_dict = models.storage.all(City)

            for key, value in cls_dict.items():
                if value.state_id == self.id:
                    list_cities.append(value)
            return list_cities
