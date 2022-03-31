import os

from pydantic import BaseModel


class AppConfig(BaseModel):
    endpoint: str


def load_from_env() -> AppConfig:
    endpoint = os.environ['ENDPOINT']
    return AppConfig(
        endpoint=endpoint,
    )


app_config = load_from_env()
endpoint = app_config.endpoint
