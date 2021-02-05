from src.models.base_model import BaseModel
from sqlalchemy import Column, Float, String
from sqlalchemy.orm import validates


class Product(BaseModel):
    __tablename__ = 'PRODUCT'
    name = Column('name', String(length=100), nullable=False)
    description = Column('description', String(length=255), nullable=True)
    price = Column('price', Float, nullable=False)

    def __init__(self, name: str, description: str, price: float) -> None:
        self.name = name
        self.description = description
        self.price = price

    @validates('name')
    def validate_name(self, key, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string!")
        if not name:
            raise ValueError("Name can't be null!")
        if len(name) > 200:
            raise ValueError("Name must have less than 200 characters.")
        return name

    @validates('description')
    def validate_description(self, key, description):
        if not isinstance(description, str):
            raise TypeError("Description must be a string!")
        if len(description) > 200:
            raise ValueError("Description must have less than 200 characters")
        return description

    @validates('price')
    def validate_price(self, key, price):
        if not isinstance(price, float):
            raise TypeError("Price must be a float number!")
        if not price:
            raise ValueError("Price can't be null!")
        if price <= 0:
            raise ValueError("Price can't be lower than 0!")
        return price
