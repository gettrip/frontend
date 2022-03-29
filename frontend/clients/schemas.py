from pydantic import BaseModel


class City(BaseModel):
    name: str


class Route(BaseModel):
    name: str
