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

cities_client = CitiesClient(endpoint)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cities')
def show_cities():
    all_cities = cities_client.get_all()
    template = env.get_template('cities.html')
    return template.render(cities=[city.dict() for city in all_cities])


@app.route('/cities/<cid>/routes/<rid>/')
def show_places_for_route(cid, rid):
    routes = {
        '1': {
            'name': 'Музеи Калининграда за 1 день',
            'places': [
                'Музей янтаря',
                'Музей Мирового океана',
                'Историко-художественный музей',
                'Музей «Бункер»',
                'Музей марципана',
                'Кенигсбергский собор'],
            'description': 'Музейная программа в городе может быть настолько насыщенной,\
             что и целого дня не хватит для основных экспозиций.'
        },
        '2': {
            'name': 'Three paks',
            'places': ['park1', 'park2', 'park3'],
            'description': 'Three paks'
        },
        '3': {
            'name': 'Two museums and a park',
            'places': ['museum1', 'park2', 'museum3'],
            'description': 'Two museums and a park'
        },
    }
    route = routes[rid]
    city_name = 'Калининград'
    route_name = route['name']
    route_description = route['description']
    places = route['places']
    template = env.get_template('route.html')
    return template.render(
        city_name=city_name,
        route_name=route_name,
        route_description=route_description,
        places=places
    )


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
