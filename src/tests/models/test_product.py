import sys

sys.path.append('.')

import pytest
from src.models.product import Product
from src.models.base_model import BaseModel

class TestProductModel:
    name = 'Cerveja'
    description = 'Cerveja do Ralph'
    price = 10.50

    def test_product_instance(self):
        products = Product(self.name, self.description, self.price)
        assert isinstance(products, Product), "Object doesn't belong to Product"
        assert isinstance(products, BaseModel), "Object doesn't belong to BaseModel"

    def test_product_empty_name(self):
        with pytest.raises(ValueError):
            product = Product('', self.description, self.price)

    def test_product_name_length(self):
        with pytest.raises(ValueError):
            product = Product(self.name*50, self.description, self.price)

    def test_product_name_type(self):
        with pytest.raises(TypeError):
            product = Product(1, self.description, self.price)

    def test_product_description_length(self):
        with pytest.raises(ValueError):
            product = Product(self.name, self.description*100, self.price)

    def test_product_description_type(self):
        with pytest.raises(TypeError):
            product = Product(self.name, 1, self.price)

    def test_product_price_type(self):
        with pytest.raises(TypeError):
            product = Product(self.name, self.description, 'Test')

    def test_product_price_greater_than_zero(self):
        with pytest.raises(ValueError):
            product = Product(self.name, self.description, -1.0)



