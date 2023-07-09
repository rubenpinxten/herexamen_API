from pydantic import BaseModel

from pydantic import BaseModel

class QuoteBase(BaseModel):
    text: str

class QuoteCreate(QuoteBase):
    name_id: int
    periode_id: int

class Quote(QuoteBase):
    id: int
    name_id: int
    periode_id: int

    class Config:
        orm_mode = True

class TitleBase(BaseModel):
    text: str

class TitleCreate(TitleBase):
    pass

class Title(TitleBase):
    id: int
    quotes: list[Quote] = []

    class Config:
        orm_mode = True

class YearBase(BaseModel):
    text: str

class YearCreate(YearBase):
    pass

class Year(YearBase):
    id: int
    spoken: list[Quote] = []

    class Config:
        orm_mode = True