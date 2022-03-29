import logging

from flask import Flask, render_template
from jinja2 import Environment, PackageLoader, select_autoescape

from frontend.clients.cities import CitiesClient
from frontend.clients.routes import RoutesClient
from frontend.config import endpoint

logger = logging.getLogger(__name__)

app = Flask(__name__)

env = Environment(
    loader=PackageLoader('frontend', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cities')
def show_cities():
    cities_client = CitiesClient(endpoint)
    all_cities = cities_client.get_all()
    template = env.get_template('cities.html')
    return template.render(cities=all_cities)


@app.route('/cities/<city_id>')
def show_routes(city_id):
    routes_client = RoutesClient(endpoint)
    city = routes_client.get_city(city_id)
    routes = routes_client.get_all(city_id)
    template = env.get_template('routes.html')
    return template.render(
        city_name=city.name,
        city_routes=[route.dict() for route in routes],
    )


def main():
    logging.basicConfig(level=logging.DEBUG)
    logger.info("Hello, world!")
    app.run()


if __name__ == '__main__':
    main()
