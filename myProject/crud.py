from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from models import Quote, Title, Year
from schemas import QuoteBase, QuoteCreate, TitleBase, TitleCreate, YearBase, YearCreate
import random
import auth
import models
import schemas

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_quote(db: Session, quote: QuoteCreate, title_text: str, year_text: str):
    db_title = db.query(Title).filter(Title.text == title_text).first()
    if not db_title:
        db_title = Title(text=title_text)
        db.add(db_title)
        db.commit()
        db.refresh(db_title)

    db_year = db.query(Year).filter(Year.text == year_text).first()
    if not db_year:
        db_year = Year(text=year_text)
        db.add(db_year)
        db.commit()
        db.refresh(db_year)

    db_quote = Quote(text=quote.text, name=db_title, periode=db_year)
    db.add(db_quote)
    db.commit()
    db.refresh(db_quote)

    return db_quote

#get quote by id
def get_quote(db: Session, quote_id: int):
    return db.query(Quote).filter(Quote.id == quote_id).first()

#get random quote between the first and the 10th
def get_quote_random(db:Session):
    id = random.randint(0,10)
    return db.query(Quote).filter(Quote.id == 6)

#update quote by id
def update_quote(db: Session, quote_id: int, quote: QuoteBase):
    db_quote = db.query(Quote).filter(Quote.id == quote_id).first()
    db_quote.text = quote.text
    db.commit()
    db.refresh(db_quote)
    return db_quote

#delete quote by id
def delete_quote(db: Session, quote_id: int):
    db_quote = db.query(Quote).filter(Quote.id == quote_id).first()
    db.delete(db_quote)
    db.commit()
    return {"message": "Quote deleted"}

#
def get_title(db: Session, title_id: int):
    return db.query(Title).filter(Title.id == title_id).first()

def delete_title(db: Session, title_id: int):
    db_title = db.query(Title).filter(Title.id == title_id).first()
    db.delete(db_title)
    db.commit()
    return {"message": "Title deleted"}

def get_year(db: Session, year_id: int):
    return db.query(Year).filter(Year.id == year_id).first()

def delete_year(db: Session, year_id: int):
    db_year = db.query(Year).filter(Year.id == year_id).first()
    db.delete(db_year)
    db.commit()
    return {"message": "Year deleted"}

def get_all_quotes(db: Session,skip:int=0,limit:int=50):
    all_quotes = db.query(models.Quote).offset(skip).limit(limit).all()
    return all_quotes

def get_all_titles(db: Session):
    return db.query(Title).all()

def get_all_years(db: Session):
    return db.query(Year).all()

# create admin
def create_admin(db: Session, admin: schemas.AdminCreate):
    hashed_password = auth.get_password_hash(admin.password)
    db_admin = models.Admin(username=admin.username, hashed_password=hashed_password)
    adminexists = db.query(models.Admin).filter(models.Admin.username == admin.username).first()
    if adminexists:
        adminerror = {
            "username": "error",
            "id": 0,
        }
        return adminerror
    else:
        db.add(db_admin)
        db.commit()
        db.refresh(db_admin)
        return db_admin

# get admin by username
def get_admin_username(db: Session, username: str):
    admin = db.query(models.Admin).filter(models.Admin.username == username).first()
    return admin

# delete admin by username
def delete_admin(db: Session, admin: schemas.Admin):
    admin = db.query(models.Admin).filter(models.Admin.username == admin.username).first()
    db.delete(admin)
    db.commit()
    return admin