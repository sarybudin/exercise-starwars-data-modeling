import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Personajes(Base):
    __tablename__ = 'personajes'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    planeta_origen = Column(Integer,ForeignKey('planetas.id'))
    estatura = Column(Integer)
    colorojos = Column(String(50))

class Vehiculos(Base):
    __tablename__ = 'vehiculos'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False) 
    modelo = Column(String(50))
    color = Column(String(50))
    conductor = Column(String(50))
    id_personaje = Column(Integer,ForeignKey('personajes.id'))
    

class Planetas(Base):
    __tablename__ = 'planetas'
    id = Column(Integer, primary_key=True)
    nombre =Column(String(50), nullable=False) 
    diametro = Column(Integer)
    poblacion = Column(Integer)
    clima = Column(String(50))
   

class FavoritoPersonajes(Base):
    __tablename__ = 'favoritopersonajes'
    id_favorito = Column(Integer, primary_key=True)
    id_usuario = Column(Integer,ForeignKey('usuario.id'))
    id_personaje = Column(Integer,ForeignKey('personajes.id'))

class FavoritoPlanetas(Base):
    __tablename__ = 'favoritoplanetas'
    id_favorito = Column(Integer, primary_key=True)
    id_usuario = Column(Integer,ForeignKey('usuario.id'))
    id_planeta = Column(Integer,ForeignKey('planetas.id'))

class FavoritoVehiculos(Base):
    __tablename__ = 'favoritovehiculos'
    id_favorito = Column(Integer, primary_key=True)
    id_usuario = Column(Integer,ForeignKey('usuario.id'))
    id_vehiculo = Column(Integer,ForeignKey('vehiculos.id'))

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nombre_usuario = Column(String(50))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')