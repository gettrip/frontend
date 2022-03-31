from flask import Blueprint, render_template

from frontend.client.api_client import gettrip


view = Blueprint('cities', __name__)


@view.route('/')
def show_cities():
    all_cities = gettrip.cities.get_all()
    return render_template(
        'cities.html',
        cities=[city.dict() for city in all_cities],
    )
