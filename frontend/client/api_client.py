from frontend.client.cities import CitiesClient
from frontend.client.routes import RoutesClient
from frontend.config import load_from_env


app_config = load_from_env()
endpoint = app_config.endpoint


class GetTripClient:

    def __init__(
        self, endpoint=endpoint,
        city_client=CitiesClient,
        route_client=RoutesClient,
    ) -> None:
        self.cities = city_client(endpoint)
        self.routes = route_client(endpoint)
