from flask import Blueprint, render_template
from .crud import Clicker

clicker_app = Blueprint('clicker_app', __name__)

clicker = Clicker()


@clicker_app.get('/', endpoint='index')
def show_clicker_page():
    return render_template('clicker/index.html', count=clicker.count)


@clicker_app.post('/', endpoint='do-click')
def handle_click():
    clicker.inc_count()
    return render_template('clicker/index.html', count=clicker.count)
