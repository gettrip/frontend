import httpx

from frontend.schemas import Route


class RoutesClient:

    def __init__(self, url: str):
        self.url = f'{url}'

    def get_for_city(self, city_id: int) -> list[Route]:
        res = httpx.get(f'{self.url}/cities/{city_id}/routes/')
        res.raise_for_status()
        routes = res.json()
        return [Route(**route) for route in routes]

    def get_by_id(self, route_id: int) -> Route:
        res = httpx.get(f'{self.url}/routes/{route_id}', follow_redirects=True)
        res.raise_for_status()
        route = Route(**res.json())
        return route
