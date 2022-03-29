import httpx

from frontend.schemas import City


class CitiesClient:

    def __init__(self, url: str):
        self.url = f'{url}/cities'

    def get_all(self) -> list[City]:
        res = httpx.get(f'{self.url}/')
        cities = res.json()
        print(cities)
        return [City(**city) for city in cities]

    def get_city(self, city_id) -> City:
        res = httpx.get(f'{self.url}/{city_id}')
        city = City(**res.json())
        return city
