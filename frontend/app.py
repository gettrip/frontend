from flask import Flask
from frontend.view import routes, cities, places, index


def create_app():
    app = Flask(__name__)

    app.register_blueprint(index.view)
    app.register_blueprint(routes.view, url_prefix='/cities')
    app.register_blueprint(cities.view, url_prefix='/cities')
    app.register_blueprint(places.view, url_prefix='/cities/<city_id>/routes')

    return app
