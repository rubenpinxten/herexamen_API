from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

import auth
import models
import schemas

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_products_for_user(db: Session, prodcut: schemas.ProductCreate, users_id: int):
    db_product = models.Product(**prodcut.dict(), owner_id=users_id)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def create_manufactors_for_products(db: Session, manufactor: schemas.ManufactorCreate, products_id: int):
    db_manufactor = models.Manufactor(**manufactor.dict(), product_id=products_id)
    db.add(db_manufactor)
    db.commit()
    db.refresh(db_manufactor)
    return db_manufactor

def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()

def get_manufactors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Manufactor).offset(skip).limit(limit).all()
    
def delete_all_manufactors(db: Session, manufactors: schemas.Manufactor):
    manufactors = db.query(models.Manufactor)
    db.delete(manufactors)
    db.commit()
    return "Alle manufactors have been deleted!"

def update_manufactors_last(db: Session, update_manufactor: schemas.ManufactorCreate):
    db_update_manufactor = db.manufactor(models.Manufactor).all()
    manufactor = db_update_manufactor[-1]
    manufactor.content = update_manufactor.content
    db.commit()
    return manufactor