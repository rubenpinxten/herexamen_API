from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials, OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware  # Import the CORSMiddleware
from passlib.context import CryptContext


import os
import secrets
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

security = HTTPBasic()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# allowed origins for CORS
origins = ["*"]

# add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"]
)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    #Try to authenticate the user
    admin = auth.authenticate_admin(db, form_data.username, form_data.password)
    if not admin:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # Add the JWT case sub with the subject(user)
    access_token = auth.create_access_token(
        data={"sub": admin.username}
    )
    #Return the JWT as a bearer token to be placed in the headers
    return {"access_token": access_token, "token_type": "bearer"}

#create quote with title and year
@app.post("/quotes/", response_model=schemas.Quote)
async def create_quote(quote_data: schemas.QuoteCreateData, db: Session = Depends(get_db)):
    quote = quote_data.quote
    title_text = quote_data.title.text
    year_text = quote_data.year.text

    db_quote = crud.create_quote(db=db, quote=quote, title_text=title_text, year_text=year_text)
    return db_quote

#get quote by id
@app.get("/quotes/{quote_id}", response_model=schemas.Quote)
async def read_quote(quote_id: int, db: Session = Depends(get_db)):
    db_quote = crud.get_quote(db=db, quote_id=quote_id)
    if db_quote is None:
        raise HTTPException(status_code=404, detail="Quote not found")
    return db_quote

#get random quote
@app.get("/quotes/random", response_model=schemas.Quote)
async def read_quote(db: Session = Depends(get_db)):
    db_quote = crud.get_quote_random(db=db)
    if db_quote is None:
        raise HTTPException(status_code=404, detail="Quote not found")
    return db_quote

#change quote by id
@app.put("/quotes/{quote_id}", response_model=schemas.Quote)
async def update_quote(quote_id: int, quote: schemas.QuoteBase, db: Session = Depends(get_db)):
    db_quote = crud.get_quote(db=db, quote_id=quote_id)
    if db_quote is None:
        raise HTTPException(status_code=404, detail="Quote not found")
    return crud.update_quote(db=db, quote_id=quote_id, quote=quote)

#delete quote by id
@app.delete("/quotes/{quote_id}")
async def delete_quote(quote_id: int, db: Session = Depends(get_db), token: str = Depends(auth.oauth2_scheme)):
    db_quote = crud.get_quote(db=db, quote_id=quote_id)
    if db_quote is None:
        raise HTTPException(status_code=404, detail="Quote not found")
    return crud.delete_quote(db=db, quote_id=quote_id)

# Title endpoints

#get title by id
@app.get("/titles/{title_id}", response_model=schemas.Title)
async def read_title(title_id: int, db: Session = Depends(get_db)):
    db_title = crud.get_title(db=db, title_id=title_id)
    if db_title is None:
        raise HTTPException(status_code=404, detail="Title not found")
    return db_title

#delete title by id
@app.delete("/titles/{title_id}")
async def delete_title(title_id: int, db: Session = Depends(get_db), token: str = Depends(auth.oauth2_scheme)):
    db_title = crud.get_title(db=db, title_id=title_id)
    if db_title is None:
        raise HTTPException(status_code=404, detail="Title not found")
    return crud.delete_title(db=db, title_id=title_id)

# Year endpoints

#get year by id
@app.get("/years/{year_id}", response_model=schemas.Year)
async def read_year(year_id: int, db: Session = Depends(get_db)):
    db_year = crud.get_year(db=db, year_id=year_id)
    if db_year is None:
        raise HTTPException(status_code=404, detail="Year not found")
    return db_year

#delete year by id
@app.delete("/years/{year_id}")
async def delete_year(year_id: int, db: Session = Depends(get_db), token: str = Depends(auth.oauth2_scheme)):
    db_year = crud.get_year(db=db, year_id=year_id)
    if db_year is None:
        raise HTTPException(status_code=404, detail="Year not found")
    return crud.delete_year(db=db, year_id=year_id)

#get all quotes
@app.get("/quotes/all", response_model=list[schemas.Quote])
async def get_all_quotes(skip: int =0, limit: int = 50, db: Session = Depends(get_db)):
    return crud.get_all_quotes(db=db,skip=skip,limit=limit)

#get all titles
@app.get("/titles/all", response_model=list[schemas.Title])
async def get_all_titles(db: Session = Depends(get_db)):
    return crud.get_all_titles(db=db)

#get all years
@app.get("/years/all", response_model=list[schemas.Year])
async def get_all_years(db: Session = Depends(get_db)):
    return crud.get_all_years(db=db)

# POST admin
@app.post("/admin", response_model=schemas.Admin)
async def create_admin(admin: schemas.AdminCreate, db: Session = Depends(get_db)):
    new_admin = crud.create_admin(db=db, admin=admin)
    return new_admin

# GET current admin
@app.get("/admin", response_model=schemas.Admin)
async def read_current_admin(db: Session = Depends(get_db), token: str = Depends(auth.oauth2_scheme)):
    current_admin = auth.get_current_admin(db, token)
    return current_admin

# GET admin by username
@app.get("/admin/{username}", response_model=schemas.Admin)
async def read_admin(username: str, db: Session = Depends(get_db)):
    admin = crud.get_admin_username(db, username)
    if admin is None:
        raise HTTPException(status_code=404, detail="Admin not found")
    return admin

# DELETE admin
@app.delete("/admin/{username}", response_model=str)
async def delete_admin(username: str, db: Session = Depends(get_db), token: str = Depends(auth.oauth2_scheme)):
    admin_username = crud.get_admin_username(db, username)
    deleted_admin = crud.delete_admin(db, admin_username)
    return "Admin: " + str(deleted_admin.username) + " deleted"