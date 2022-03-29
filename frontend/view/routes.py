from flask import Blueprint, render_template

from frontend import routes_client, cities_client

view = Blueprint('routes', __name__)


@view.get('/<city_id>')
def show_routes(city_id):
    city = cities_client.get_city(city_id)
    routes = routes_client.get_all(city_id)

    return render_template(
        'routes.html',
        city_name=city.name,
        city_routes=[route.dict() for route in routes],
    )
