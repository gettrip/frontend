import httpx


class CitiesClient:
    def __init__(self, url: str):
        self.url = f'{url}/cities'

    def get_all(self):
        res = httpx.get(f'{self.url}/')
        return res.json()
