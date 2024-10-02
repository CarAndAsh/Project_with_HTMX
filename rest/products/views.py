from dataclasses import asdict
from http import HTTPStatus
from time import sleep

from flask import (Blueprint, render_template, request, Response, redirect, url_for)
from werkzeug.exceptions import HTTPException, NotFound

from .crud import products_storage
from .forms import ProductForm

products_app = Blueprint('products_app', __name__)


@products_app.get('/', endpoint='list')
def get_products_list():
    form = ProductForm()
    products = products_storage.get_list()
    return render_template('products/list.html', products=products, form=form)


@products_app.post('/', endpoint='create')
def create_product():
    form = ProductForm()
    if not form.validate_on_submit():
        response = Response(render_template('products/components/form.html',
                                            form=form),
                            status=HTTPStatus.UNPROCESSABLE_ENTITY, )
        raise HTTPException(response=response)
    product = products_storage.add(form.name.data, form.price.data)
    return render_template('products/components/form-and-item-oob.html', form=ProductForm(formdata=None),
                           product=product)


def get_product(product_id: int):
    product = products_storage.get_by_id(product_id)
    if product:
        return product
    raise NotFound(f'Product with id - {product_id} does not exist!')


@products_app.get('/<int:product_id>/', endpoint='details')
def get_product_details(product_id: int):
    product = get_product(product_id)
    return render_template('products/details.html',
                           form=ProductForm(data=asdict(product)),
                           product=product)


@products_app.put('/<int:product_id>/', endpoint='update')
def update_product(product_id: int):
    product = get_product(product_id)
    print(product_id)
    form = ProductForm()
    if not form.validate_on_submit():
        response = Response(render_template('products/components/form-update.html',
                                            form=form, product=product),
                            status=HTTPStatus.UNPROCESSABLE_ENTITY, )
        raise HTTPException(response=response)
    products_storage.update(product_id=product.id,
                            product_name=form.name.data,
                            product_price=form.price.data)
    return render_template('products/components/form-update.html', form=form, product=product)


@products_app.delete('/<int:product_id>/', endpoint='delete')
def delete_product(product_id: int):
    sleep(2)  # only for watching how animation works
    products_storage.delete(product_id)
    if not request.args.get('redirect'):
        return Response(status=HTTPStatus.NO_CONTENT)
    return redirect(url_for('products_app.list'), HTTPStatus.SEE_OTHER)
