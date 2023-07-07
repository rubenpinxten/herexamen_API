from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

import os

import auth
import crud
import models
import schemas
from database import SessionLocal, engine


if not os.path.exists('.\sqlitedb'):
    os.makedirs('.\sqlitedb')

#"sqlite:///./sqlitedb/sqlitedata.db"
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = auth.create_access_token(
        data={"sub": user.email}
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/users/create/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.get("/users/me", response_model=schemas.User)
def read_users_me(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    current_user = auth.get_current_active_user(db, token)
    return current_user

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/products/", response_model=schemas.Product)
def create_products_user(user_id: int, product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_products_for_user(db=db, product=product, user_id=user_id)


@app.post("/products/{product_id}/manufactors/", response_model=schemas.Manufactor)
def create_manufactors_products(product_id: int, manufactor: schemas.ManufactorCreate, db: Session = Depends(get_db)):
    return crud.create_manufactors_for_products(db=db, manufactor=manufactor, product_id=product_id)


@app.get("/Products/", response_model=list[schemas.Product])
def read_Products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = crud.get_products(db, skip=skip, limit=limit)
    return products


@app.get("/manufactors/", response_model=list[schemas.Manufactor])
def read_manufactors(skip: int = 0, limit: int = 100, db: Session= Depends(get_db)):
    manufactors = crud.get_manufactors(db, skip=skip, limit=limit)
    return manufactors

@app.put("/update/manufactor/last", response_model=list[schemas.Manufactor])
async def update():
    crud.update_manufactors_last()
    return ("DB has been updated")

@app.delete("/delete/manufactors", response_model=list[schemas.Manufactor])
async def delete():
    crud.delete_all_manufactors()
    return ("All manufactors have been deleted")