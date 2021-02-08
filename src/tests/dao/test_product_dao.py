import sys

sys.path.append('.')

import pytest
from src.models.product import Product
from src.dao.product_dao import ProductDao
from sqlalchemy.orm.exc import UnmappedInstanceError

class TestProductDao:
    dao = ProductDao()

    @pytest.fixture
    def create_instance(self):
        product = Product('Cerveja', 'Cerveja do Ralph', 10.50)
        return product

    def test_instance(self):
        assert isinstance(self.dao, ProductDao)

    def test_save(self, create_instance):
        product_saved = self.dao.save(create_instance)
        assert product_saved.id_ is not None
        self.dao.delete(product_saved)

    def test_read_by_id(self, create_instance):
        product_saved = self.dao.save(create_instance)
        product_read = self.dao.read_by_id(product_saved.id_)
        assert isinstance(product_read, Product)
        self.dao.delete(product_saved)

    def test_not_read_by_id(self):
        with pytest.raises(TypeError):
            self.dao.read_by_id('id')

    def test_read_all(self):
        result = self.dao.read_all()
        assert isinstance(result, list)

    def test_delete(self, create_instance):
        product_saved = self.dao.save(create_instance)
        product_read = self.dao.read_by_id(product_saved.id_)
        self.dao.delete(product_read)
        product_read = self.dao.read_by_id(product_saved.id_)
        assert product_read is None

    def test_not_save(self):
        with pytest.raises(UnmappedInstanceError):
            self.dao.save('Cerveja')

    def test_not_delete(self):
        with pytest.raises(UnmappedInstanceError):
            self.dao.delete('String Qualquer')
