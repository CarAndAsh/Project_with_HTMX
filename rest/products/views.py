from flask import (Blueprint, render_template, request, redirect, url_for)

from .crud import products_storage

products_app = Blueprint('products_app', __name__)


@products_app.get('/', endpoint='list')
def get_products_list():
    products = products_storage.get_list()
    return render_template('products/list.html', products=products)


@products_app.post('/', endpoint='create')
def create_product():
    product_name = request.form.get('product-name', '').strip()
    product_price = request.form.get('product-price', '1').strip()
    product = products_storage.add(product_name, int(product_price))
    return render_template('products/components/item-oob.html', product=product)
