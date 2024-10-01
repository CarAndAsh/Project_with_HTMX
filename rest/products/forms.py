from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange, ValidationError

from .crud import products_storage


def validate_product_name(form, field):
    product_name = field.data
    # TODO update: check same id
    if request.method == 'POST' and products_storage.name_exist(product_name):
        raise ValidationError(f'Product with {product_name!r} alrady exist!')


class ProductForm(FlaskForm):
    name = StringField(label='Product :', validators=[DataRequired(), validate_product_name])
    price = IntegerField(label='Price :', validators=[DataRequired(), NumberRange(1, 9999)])
    add = SubmitField('Add product')
    update = SubmitField('Update product details')
