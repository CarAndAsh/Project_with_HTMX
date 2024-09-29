from http import HTTPStatus

from flask import (Blueprint, render_template, request, Response)
from werkzeug.exceptions import HTTPException

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
    if not product_price.isnumeric():
        response = Response(render_template('products/components/form.html',
                                            product_name=product_name,
                                            error='Product price should be integer'),
                            status=HTTPStatus.UNPROCESSABLE_ENTITY, )
        raise HTTPException(response=response)
    product = products_storage.add(product_name, int(product_price))
    return render_template('products/components/form-and-item-oob.html', product=product)
