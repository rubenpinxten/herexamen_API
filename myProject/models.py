from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class Quote(Base):
    __tablename__ = "quotes"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    name_id = Column(Integer, ForeignKey("titles.id"))
    periode_id = Column(Integer, ForeignKey("years.id"))

    name = relationship("Title", back_populates="quote")
    periode = relationship("Year", back_populates="spoken")

class Title(Base):
    __tablename__ = "titles"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)

    quote = relationship("Quote", back_populates="name")

class Year(Base):
    __tablename__ = "years"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)

    spoken = relationship("Quote", back_populates="periode")

class Admin(Base):
    __tablename__ = "admins"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

