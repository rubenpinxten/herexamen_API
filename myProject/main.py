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

@app.post("/quotes/", response_model=schemas.Quote)
def create_quote(quote_data: schemas.QuoteCreateData, db: Session = Depends(get_db)):
    quote = quote_data.quote
    title_text = quote_data.title.text
    year_text = quote_data.year.text

    db_quote = crud.create_quote(db=db, quote=quote, title_text=title_text, year_text=year_text)
    return db_quote

@app.get("/quotes/{quote_id}", response_model=schemas.Quote)
def read_quote(quote_id: int, db: Session = Depends(get_db)):
    db_quote = crud.get_quote(db=db, quote_id=quote_id)
    if db_quote is None:
        raise HTTPException(status_code=404, detail="Quote not found")
    return db_quote

@app.put("/quotes/{quote_id}", response_model=schemas.Quote)
def update_quote(quote_id: int, quote: schemas.QuoteBase, db: Session = Depends(get_db)):
    db_quote = crud.get_quote(db=db, quote_id=quote_id)
    if db_quote is None:
        raise HTTPException(status_code=404, detail="Quote not found")
    return crud.update_quote(db=db, quote_id=quote_id, quote=quote)

@app.delete("/quotes/{quote_id}")
def delete_quote(quote_id: int, db: Session = Depends(get_db)):
    db_quote = crud.get_quote(db=db, quote_id=quote_id)
    if db_quote is None:
        raise HTTPException(status_code=404, detail="Quote not found")
    return crud.delete_quote(db=db, quote_id=quote_id)

# Title endpoints

@app.post("/titles/", response_model=schemas.Title)
def create_title(title: schemas.TitleCreate, db: Session = Depends(get_db)):
    return crud.create_title(db=db, title=title)

@app.get("/titles/{title_id}", response_model=schemas.Title)
def read_title(title_id: int, db: Session = Depends(get_db)):
    db_title = crud.get_title(db=db, title_id=title_id)
    if db_title is None:
        raise HTTPException(status_code=404, detail="Title not found")
    return db_title

@app.put("/titles/{title_id}", response_model=schemas.Title)
def update_title(title_id: int, title: schemas.TitleBase, db: Session = Depends(get_db)):
    db_title = crud.get_title(db=db, title_id=title_id)
    if db_title is None:
        raise HTTPException(status_code=404, detail="Title not found")
    return crud.update_title(db=db, title_id=title_id, title=title)

@app.delete("/titles/{title_id}")
def delete_title(title_id: int, db: Session = Depends(get_db)):
    db_title = crud.get_title(db=db, title_id=title_id)
    if db_title is None:
        raise HTTPException(status_code=404, detail="Title not found")
    return crud.delete_title(db=db, title_id=title_id)

# Year endpoints

@app.post("/years/", response_model=schemas.Year)
def create_year(year: schemas.YearCreate, db: Session = Depends(get_db)):
    return crud.create_year(db=db, year=year)

@app.get("/years/{year_id}", response_model=schemas.Year)
def read_year(year_id: int, db: Session = Depends(get_db)):
    db_year = crud.get_year(db=db, year_id=year_id)
    if db_year is None:
        raise HTTPException(status_code=404, detail="Year not found")
    return db_year

@app.put("/years/{year_id}", response_model=schemas.Year)
def update_year(year_id: int, year: schemas.YearBase, db: Session = Depends(get_db)):
    db_year = crud.get_year(db=db, year_id=year_id)
    if db_year is None:
        raise HTTPException(status_code=404, detail="Year not found")
    return crud.update_year(db=db, year_id=year_id, year=year)

@app.delete("/years/{year_id}")
def delete_year(year_id: int, db: Session = Depends(get_db)):
    db_year = crud.get_year(db=db, year_id=year_id)
    if db_year is None:
        raise HTTPException(status_code=404, detail="Year not found")
    return crud.delete_year(db=db, year_id=year_id)

@app.get("/quotes/get/", response_model=list[schemas.Quote])
def get_all_quotes(db: Session = Depends(get_db)):
    return crud.get_all_quotes(db=db)

@app.get("/titles/get/", response_model=list[schemas.Title])
def get_all_titles(db: Session = Depends(get_db)):
    return crud.get_all_titles(db=db)

@app.get("/years/get/", response_model=list[schemas.Year])
def get_all_years(db: Session = Depends(get_db)):
    return crud.get_all_years(db=db)