import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'dog'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

    

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(50), unique=True)

class Starships(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    fav_starship = Column(Integer, ForeignKey('fav_starships.id'))
    fav_starship_relationship = relationship("Fav_tarships", uselist=False)

class Fav_Starships(Base):
    __tablename__ = 'fav_starships'
    id = Column(Integer, primary_key=True)
    starship = Column(Integer, ForeignKey('starships.id'))
    starship_relationship = relationship(Starships)
    user = Column(Integer, ForeignKey('users.id'))
    user_relationship = relationship(Users)
    
    
class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    rotation_period = Column(Integer)
    diameter = Column(Integer)
    rotation_period = Column(Integer)
    gravity = Column(String(50))
    population = Column(Integer)
    climate = Column(String(50))
    terrain = Column(String(50))
    surface_water = Column(Integer)
    fav_planet = Column(Integer, ForeignKey('fav_planets.id'))
    fav_planet_relationship = relationship("Fav_planets", uselist=False)

class Fav_Planets(Base):
    __tablename__ = 'fav_planets'
    id = Column(Integer, primary_key=True)
    planet = Column(Integer, ForeignKey('planets.id'))
    planet_relationship = relationship(Planets)
    user = Column(Integer, ForeignKey('users.id'))
    user_relationship = relationship(Users)
    
class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    mass = Column(Integer)
    height = Column(Integer)
    hair_color = Column(String(50))
    skin_color = Column(String(50))
    eye_color = Column(String(50))
    birth_year = Column(String(50))
    gender = Column(String(50))
    planet = Column(Integer, ForeignKey('planets.id'))
    planet_relationship = relationship(Planets)
    starship = Column(Integer, ForeignKey('starships.id'))
    starship_relationship = relationship(Starships)
    fav_character = Column(Integer, ForeignKey('fav_characters.id'))
    fav_character_relationship = relationship("Fav_Characters", uselist=False)
    

class Fav_Characters(Base):
    __tablename__ = 'fav_characters'
    id = Column(Integer, primary_key=True)
    character = Column(Integer, ForeignKey('characters.id'))
    character_relationship = relationship(Characters, uselist=False)
    user = Column(Integer, ForeignKey('users.id'))
    user_relationship = relationship(Users)

    def to_dict(self):
        return {
        }
    
# The to_dict method can be useful when you want to serialize an instance of the Users class into a JSON-like dictionary representation, for example, when working with APIs or storing data in a database.


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')




