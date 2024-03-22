#!/usr/bin/python3
"""Defines the City class"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from relationship_state import Base


class City(Base):
    """City class to represent cities in a database"""

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State", back_populates="cities")

    def __repr__(self):
        """ __repr """"
        return "<City(id='%s', name='%s', state_id='%s')>" % (
            self.id, self.name, self.state_id)
