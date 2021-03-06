from flask import Blueprint, render_template

from frontend.client.api import gettrip


view = Blueprint('routes', __name__)


@view.get('/<city_id>')
def show_routes(city_id):
    city = gettrip.cities.get_by_id(city_id)
    routes = gettrip.routes.get_for_city(city_id)

    return render_template(
        'routes.html',
        city_name=city.name,
        city_id=city.uid,
        city_routes=[route.dict() for route in routes],
    )
