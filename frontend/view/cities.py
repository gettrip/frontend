from flask import Blueprint, render_template

from frontend import cities_client

view = Blueprint('cities', __name__)


@view.route('/')
def show_cities():
    all_cities = cities_client.get_all()

    return render_template(
        'cities.html',
        cities=[city.dict() for city in all_cities],
    )
