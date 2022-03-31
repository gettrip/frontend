from flask import Blueprint, render_template

from frontend.client.api_client import GetTripClient
from frontend.config import load_from_env


app_config = load_from_env()
endpoint = app_config.endpoint


view = Blueprint('cities', __name__)

gettrip = GetTripClient(endpoint)


@view.route('/')
def show_cities():
    all_cities = gettrip.cities.get_all()
    return render_template(
        'cities.html',
        cities=[city.dict() for city in all_cities],
    )
