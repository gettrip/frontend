from flask import Flask
from frontend.view import routes, cities, places, index
from frontend.client.routes import RoutesClient
from frontend.client.cities import CitiesClient
from frontend.config import load_from_env

app_config = load_from_env()
endpoint = app_config.endpoint

routes_client = RoutesClient(endpoint)
cities_client = CitiesClient(endpoint)


def create_app():
    app = Flask(__name__)

    app.register_blueprint(index.view)
    app.register_blueprint(routes.view, url_prefix='/cities')
    app.register_blueprint(cities.view, url_prefix='/cities')
    app.register_blueprint(places.view, url_prefix='/cities/<city_id>/routes')

    return app
