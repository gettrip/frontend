from flask import Blueprint, render_template

from frontend.client.cities import CitiesClient
from frontend.config import load_from_env

app_config = load_from_env()
endpoint = app_config.endpoint

cities_client = CitiesClient(endpoint)

view = Blueprint('cities', __name__)


@view.route('/')
def show_cities():
    all_cities = cities_client.get_all()

    return render_template(
        'cities.html',
        cities=[city.dict() for city in all_cities],
    )
