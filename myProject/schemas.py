from pydantic import BaseModel

class QuoteBase(BaseModel):
    text: str

class QuoteCreate(QuoteBase):
    pass

class TitleBase(BaseModel):
    text: str

class TitleCreate(TitleBase):
    pass

class YearBase(BaseModel):
    text: str

class YearCreate(YearBase):
    pass

class QuoteCreateData(BaseModel):
    quote: QuoteCreate
    title: TitleCreate
    year: YearCreate