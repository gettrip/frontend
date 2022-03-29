from frontend.client.routes import RoutesClient
from frontend.client.cities import CitiesClient
from frontend.config import load_from_env

app_config = load_from_env()
endpoint = app_config.endpoint

routes_client = RoutesClient(endpoint)
cities_client = CitiesClient(endpoint)

__all__ = ['routes_client', 'cities_client']
