from flask import Blueprint, render_template

index_app = Blueprint('index_app', __name__)


@index_app.route('/', endpoint='index')
def index_view():
    return render_template('index.html')
