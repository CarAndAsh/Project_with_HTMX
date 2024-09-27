from flask import Blueprint, render_template, request

from .crud import product_storage

products_app = Blueprint('products_app', __name__)


@products_app.get('/', endpoint='list')
def get_products_list():
    products = product_storage.get_list()
    return render_template('products/list.html', products=products)
