from flask import Blueprint, render_template, request
from csrf_protection import csrf
examples_app = Blueprint('examples_app', __name__)


@examples_app.get('/', endpoint='index')
def examples_list():
    return render_template('examples/index.html')


@examples_app.route('/ping/', methods=['GET', 'POST'], endpoint='ping')
@csrf.exempt
def handle_ping():
    if request.method == 'POST':
        return 'pong!'
    return render_template('examples/ping/show-ping.html')


@examples_app.route('/pong/', methods=['GET', 'POST'], endpoint='pong')
def handle_ctrl_ping():
    if request.method == 'POST':
        return 'control pong!'
    return render_template('examples/ping/show-ping.html')


@examples_app.route('/hover/', methods=['GET', 'POST'], endpoint='hover')
def handle_hover():
    if request.method == 'POST':
        return "Now this text is in tag upper level (check F12 =) )"
    return render_template('examples/hover/show-hover.html')
