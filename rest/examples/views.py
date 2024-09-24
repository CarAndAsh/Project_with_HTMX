from flask import Blueprint, render_template, request

examples_app = Blueprint('examples_app', __name__)


@examples_app.get('/', endpoint='index')
def examples_list():
    return render_template('examples/index.html')


@examples_app.route('/ping/', methods=['GET', 'POST'], endpoint='ping')
def handle_ping():
    if request.method == 'POST':
        return 'pong!'
    return render_template('examples/ping/show-ping.html')
