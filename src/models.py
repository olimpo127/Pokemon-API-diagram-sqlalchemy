import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

#class Person(Base):
    #__tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    #id = Column(Integer, primary_key=True)
    #name = Column(String(250), nullable=False)

#class Address(Base):
    #__tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    #id = Column(Integer, primary_key=True)
    #street_name = Column(String(250))
    #street_number = Column(String(250))
    #post_code = Column(String(250), nullable=False)
    #person_id = Column(Integer, ForeignKey('person.id'))
    #person = relationship(Person)

class Pokemon(Base):
    __tablename__ = "pokemon"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    feature = relationship("Feature", back_populates="pokemon")
    stat = relationship("Stat", back_populates="pokemon")

class Feature(Base):
    __tablename__ = "feature"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    type1 = Column(String(20), nullable=False)
    type2 = Column(String(20))
    height = Column(Integer)
    weight = Column(Integer)
    ability1 = Column(String(50), nullable=False)
    ability2 = Column(String(50))
    ability3 = Column(String(50))
    parent_id = Column(Integer, ForeignKey("pokemon.id"))

class Stat(Base):
    __tablename__ = "stat"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False) 
    hp = Column(Integer, nullable=False)
    attack = Column(Integer, nullable=False)
    defense = Column(Integer, nullable=False)
    special_atk = Column(Integer, nullable=False)
    special_def = Column(Integer, nullable=False)
    speed = Column(Integer, nullable=False)
    parent_id = Column(Integer, ForeignKey("pokemon.id"))



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
