from typing import Dict


class RoutesClient:
    def __init__(self):
        self.cities: Dict[str, dict] = {
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

    def get_all(self, city) -> Dict:
        res = self.cities[city]
        return res
