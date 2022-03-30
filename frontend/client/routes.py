import httpx

from frontend.schemas import Route


class RoutesClient:

    def __init__(self, url: str):
        self.url = f'{url}/cities'

    def get_for_city(self, city_id: int) -> list[Route]:
        res = httpx.get(f'{self.url}/{city_id}/routes/')
        routes = res.json()
        return [Route(**route) for route in routes]
