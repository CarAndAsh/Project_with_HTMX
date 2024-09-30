from flask import Flask

from csrf_protection import csrf
from rest.index import index_app
from rest.examples import examples_app
from rest.clicker import clicker_app
from rest.products import products_app


def create_app():
    app = Flask(__name__)
    app.config.update(SECRET_KEY='this@#really?|secret&*key&*')
    csrf.init_app(app)
    app.register_blueprint(index_app)
    app.register_blueprint(examples_app, url_prefix='/examples')
    app.register_blueprint(clicker_app, url_prefix='/clicker')
    app.register_blueprint(products_app, url_prefix='/products')
    return app


def main():
    app = create_app()
    app.run(debug=True)


if __name__ == '__main__':
    main()
