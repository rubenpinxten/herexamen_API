from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    products = relationship("Product", back_populates="owner")


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="products")

    manufactors = relationship("Manufactor", back_populates="product")


class Manufactor(Base):
    __tablename__ = "manufactors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))

    product = relationship("Product", back_populates="manufactors")