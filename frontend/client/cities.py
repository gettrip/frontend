import httpx

from frontend.schemas import City


class CitiesClient:

    def __init__(self, url: str):
        self.url = f'{url}/cities'

    def get_all(self) -> list[City]:
        res = httpx.get(f'{self.url}/')
        res.raise_for_status()
        cities = res.json()
        return [City(**city) for city in cities]

    def get_by_id(self, city_id: int) -> City:
        res = httpx.get(f'{self.url}/{city_id}')
        res.raise_for_status()
        city = City(**res.json())
        return city
