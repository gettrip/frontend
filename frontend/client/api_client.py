from frontend.client.cities import CitiesClient
from frontend.client.routes import RoutesClient


class GetTripClient:

    def __init__(self, endpoint: str) -> None:
        self.cities = CitiesClient(endpoint)
        self.routes = RoutesClient(endpoint)
