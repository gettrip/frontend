import httpx

from frontend.schemas import RoutePoint


class PlacesClient:

    def __init__(self, url: str):
        self.url = f'{url}/routes'

    def get_points(self, route_id: int) -> list[RoutePoint]:
        res = httpx.get(f'{self.url}/{route_id}/points/')
        res.raise_for_status()
        points = res.json()
        return [RoutePoint(**point) for point in points]
