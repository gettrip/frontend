from frontend.client.cities import CitiesClient
from frontend.client.routes import RoutesClient
from frontend.client.places import PlacesClient
from frontend.config import config


class GetTripClient:

    def __init__(self, endpoint: str) -> None:
        self.cities = CitiesClient(endpoint)
        self.routes = RoutesClient(endpoint)
        self.places = PlacesClient(endpoint)


gettrip = GetTripClient(config.endpoint)
