from flask import Blueprint, render_template

from frontend.client.api import gettrip

view = Blueprint('places', __name__)


@view.route('/<route_id>/places')
def show_places_for_route(city_id, route_id):
    route = gettrip.routes.get_by_id(route_id)
    route_name = route.name
    route_image = route.image
    route_description = route.description
    route_duration = round(route.duration / 3600)

    city = gettrip.cities.get_by_id(city_id)
    city_name = city.name

    route_points = gettrip.places.get_points(route_id)
    for point in route_points:
        point.place.duration = round(point.place.duration / 60)

    return render_template(
        'route_places.html',
        city_name=city_name,
        city_id=city_id,
        route_points=route_points,
        route_name=route_name,
        route_image=route_image,
        route_description=route_description,
        route_duration=route_duration
    )
