#!/usr/bin/python3
"""class definition of a State"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import City
from relationship_city import Base


class State(Base):
    """state class"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

    cities = relationship(
        "City", back_populates="state", cascade="all, delete")
