from pydantic import BaseModel

class ManufactorBase(BaseModel):
    name: str

class ManufactorCreate(ManufactorBase):
    pass

class Manufactor(ManufactorBase):
    id: int
    product_id: int

    class Config:
        orm_mode = True

class ProductBase(BaseModel):
    name: str


class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    user_id :int
    manufactors: list[ManufactorBase] = []

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    products: list[ProductBase] = []

    class Config:
        orm_mode = True