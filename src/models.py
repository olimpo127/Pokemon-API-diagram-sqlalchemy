import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    favorite = relationship("Favorite")

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
    pokemon_id = Column(Integer)
    name = Column(String(50), nullable=False)
    is_favorite = Column(Boolean)
    feature = relationship("Feature", back_populates="pokemon")
    stat = relationship("Stat", back_populates="pokemon")
    favorite = relationship("Favorite")

class Feature(Base):
    __tablename__ = "feature"
    id = Column(Integer, primary_key=True)
    pokemon_id = Column(Integer)
    name = Column(String(50), nullable=False)
    type1 = Column(String(20), nullable=False)
    type2 = Column(String(20))
    height = Column(Integer)
    weight = Column(Integer)
    ability1 = Column(String(50), nullable=False)
    ability2 = Column(String(50))
    ability3 = Column(String(50))
    parent_id = Column(Integer, ForeignKey("pokemon.pokemon_id"))

class Stat(Base):
    __tablename__ = "stat"
    id = Column(Integer, primary_key=True)
    pokemon_id = Column(Integer)
    name = Column(String(50), nullable=False) 
    hp = Column(Integer, nullable=False)
    attack = Column(Integer, nullable=False)
    defense = Column(Integer, nullable=False)
    special_atk = Column(Integer, nullable=False)
    special_def = Column(Integer, nullable=False)
    speed = Column(Integer, nullable=False)
    parent_id = Column(Integer, ForeignKey("pokemon.pokemon_id"))

class Favorite(Base):
    __tablename__ = "favorite"
    id = Column(Integer, primary_key=True)
    pokemon_id = Column(Integer)
    name = Column(String(50), nullable=False) 
    parent_id = Column(Integer, ForeignKey("pokemon.pokemon_id"))
    parent_id = Column(Integer, ForeignKey("user.id"))



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
