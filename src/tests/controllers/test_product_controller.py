import sys

sys.path.append('.')

import pytest
from src.controllers.base_controller import BaseController
from src.controllers.product_controller import ProductController
from src.models.product import Product

class TestProductController:

    @pytest.fixture
    def create_instance(self):
        product = ProductController()
        return product

    def test_product_controller_instance(self, create_instance):
        assert isinstance(create_instance, BaseController)
        assert isinstance(create_instance, ProductController)

    def test_read_all_should_return_list(self, create_instance):
        result = create_instance.read_all()
        assert isinstance(result, list)

    def test_read_by_id_with_invalid_id_should_raise_exception(self, create_instance):
        with pytest.raises(Exception) as exc:
            create_instance.read_by_id(3129313)
        assert str(exc.value) == 'Object not found!'

    def test_read_by_id_should_return_product(self, create_instance):
        product = Product('Nome', 'Descrição', 10.0)
        product_created = create_instance.create(product)
        product_read = create_instance.read_by_id(product_created.id_)
        assert isinstance(product_read, Product)
        create_instance.delete(product_created)

    def test_update_should_return_product_updated(self, create_instance):
        product = Product('Nome', 'Descrição', 10.0)
        product_created = create_instance.create(product)
        product_created.name = 'Novo Nome'
        product_created.description = 'Nova Descrição'
        product_updated = create_instance.update(product_created)
        assert product_updated.id_ == product_created.id_
        assert product_updated.name == 'Novo Nome'
        assert product_updated.description == 'Nova Descrição'
        create_instance.delete(product_updated)
