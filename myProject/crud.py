from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from .models import Quote, Title, Year
from .schemas import QuoteBase, QuoteCreate, TitleBase, TitleCreate, YearBase, YearCreate


import auth
import models
import schemas

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_quote(db: Session, quote: schemas.QuoteCreate):
    db_quote = models.Quote(text=quote.text, name_id=quote.name_id, periode_id=quote.periode_id)
    db.add(db_quote)
    db.commit()
    db.refresh(db_quote)
    return db_quote

def get_quote(db: Session, quote_id: int):
    return db.query(Quote).filter(Quote.id == quote_id).first()

def update_quote(db: Session, quote_id: int, quote: QuoteBase):
    db_quote = db.query(Quote).filter(Quote.id == quote_id).first()
    db_quote.text = quote.text
    db.commit()
    db.refresh(db_quote)
    return db_quote

def delete_quote(db: Session, quote_id: int):
    db_quote = db.query(Quote).filter(Quote.id == quote_id).first()
    db.delete(db_quote)
    db.commit()
    return {"message": "Quote deleted"}

def create_title(db: Session, title: TitleCreate):
    db_title = Title(text=title.text)
    db.add(db_title)
    db.commit()
    db.refresh(db_title)
    return db_title

def get_title(db: Session, title_id: int):
    return db.query(Title).filter(Title.id == title_id).first()

def update_title(db: Session, title_id: int, title: TitleBase):
    db_title = db.query(Title).filter(Title.id == title_id).first()
    db_title.text = title.text
    db.commit()
    db.refresh(db_title)
    return db_title

def delete_title(db: Session, title_id: int):
    db_title = db.query(Title).filter(Title.id == title_id).first()
    db.delete(db_title)
    db.commit()
    return {"message": "Title deleted"}

def create_year(db: Session, year: YearCreate):
    db_year = Year(text=year.text)
    db.add(db_year)
    db.commit()
    db.refresh(db_year)
    return db_year

def get_year(db: Session, year_id: int):
    return db.query(Year).filter(Year.id == year_id).first()

def update_year(db: Session, year_id: int, year: YearBase):
    db_year = db.query(Year).filter(Year.id == year_id).first()
    db_year.text = year.text
    db.commit()
    db.refresh(db_year)
    return db_year

def delete_year(db: Session, year_id: int):
    db_year = db.query(Year).filter(Year.id == year_id).first()
    db.delete(db_year)
    db.commit()
    return {"message": "Year deleted"}