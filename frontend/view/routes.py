from flask import Blueprint, render_template

from frontend.client.routes import RoutesClient
from frontend.client.cities import CitiesClient
from frontend.config import load_from_env

app_config = load_from_env()
endpoint = app_config.endpoint

routes_client = RoutesClient(endpoint)
cities_client = CitiesClient(endpoint)

view = Blueprint('routes', __name__)


@view.get('/<city_id>')
def show_routes(city_id):
    city = cities_client.get_by_id(city_id)
    routes = routes_client.get_for_city(city_id)

    return render_template(
        'routes.html',
        city_name=city.name,
        city_routes=[route.dict() for route in routes],
    )
