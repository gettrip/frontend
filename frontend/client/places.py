import httpx

from frontend.schemas import Place


class PlacesClient:

    def __init__(self, url: str):
        self.url = f'{url}/routes'

    def get_for_route(self, route_id: int) -> list[Place]:
        res = httpx.get(f'{self.url}/{route_id}/places/')
        res.raise_for_status()
        places = res.json()
        return [Place(**place) for place in places]
