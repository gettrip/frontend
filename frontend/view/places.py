from flask import Blueprint, render_template

from frontend.client.api import gettrip

view = Blueprint('places', __name__)


@view.route('/<route_id>/places')
def show_places_for_route(city_id, route_id):
    route = gettrip.routes.get_by_id(route_id)
    route_name = route.name

    city = gettrip.cities.get_by_id(city_id)
    city_name = city.name

    places = gettrip.places.get_for_route(route_id)

    return render_template(
        'places_on_route.html',
        city_name=city_name,
        city_id=city_id,
        places=places,
        route_name=route_name,
    )
