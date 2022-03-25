import logging

from flask import Flask, render_template
from jinja2 import Environment, PackageLoader, select_autoescape

from frontend.clients.cities import CitiesClient
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


def main():
    logging.basicConfig(level=logging.DEBUG)
    logger.info("Hello, world!")
    app.run()


if __name__ == '__main__':
    main()
