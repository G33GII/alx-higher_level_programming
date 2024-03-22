#!/usr/bin/python3
"""Defines the State class"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class to represent states in a database"""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete",
                          back_populates="state")

    def __repr__(self):
        return "<State(id='%s', name='%s')>" % (self.id, self.name)
