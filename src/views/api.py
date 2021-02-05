from flask import Flask
from flask_restful import Api
from src.resources.product_resource import ProductResource

app = Flask(__name__)
api = Api(app)

api.add_resource(ProductResource, '/api/product', endpoint='products')
api.add_resource(ProductResource, '/api/product/<int:id>', endpoint='product')


@app.route('/')
def index():
    return "Welcome"


app.run(debug=True)
