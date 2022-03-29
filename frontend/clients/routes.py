import logging
import httpx
from frontend.clients.schemas import Route, City

logger = logging.getLogger(__name__)


class RoutesClient:

    def __init__(self, url: str):
        self.url = f'{url}/cities'

        self.cities: dict[str, dict] = {
            'moscow': {
                'city_name': 'Москва',
                'routes': ['Музеи Москвы', 'Памятники', 'Парки', 'Рестораны', 'Телебашни']
            },
            'paris': {
                'city_name': 'Париж',
                'routes': ['Музеи Парижа', 'Памятники', 'Парки', 'Рестораны', 'Соборы']
            },
            'berlin': {
                'city_name': 'Берлин',
                'routes': ['Музеи Берлина', 'Памятники', 'Парки', 'Рестораны']
            },

        }

    def get_city(self, city_id) -> City:
        res = httpx.get(f'{self.url}/{city_id}')
        city = City(**res.json())
        return city

    def get_all(self, city_id) -> list[Route]:
        res = httpx.get(f'{self.url}/{city_id}/routes/')
        routes = res.json()
        return [Route(**route) for route in routes]
