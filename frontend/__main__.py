import logging

from flask import Flask, render_template
from jinja2 import Environment, PackageLoader, select_autoescape

logger = logging.getLogger(__name__)

app = Flask(__name__)

cities = [
    {'uid': 1, 'city_name': 'Yekaterinburg'},
    {'uid': 2, 'city_name': 'Moscow'},
    {'uid': 3, 'city_name': 'Toronto'},
    {'uid': 4, 'city_name': 'London'},
    {'uid': 5, 'city_name': 'Prague'},
]

env = Environment(
    loader=PackageLoader('frontend', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cities')
def show_cities():
    template = env.get_template('cities.html')
    return template.render(cities=cities)


def main():
    logging.basicConfig(level=logging.DEBUG)
    logger.info("Hello, world!")
    app.run()


if __name__ == '__main__':
    main()
