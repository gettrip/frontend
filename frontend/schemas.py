from pydantic import BaseModel


class City(BaseModel):
    uid: int
    name: str
    image: str


class Route(BaseModel):
    uid: int
    name: str
    city_id: int
    image: str
    description: str


class Place(BaseModel):
    name: str
    image: str
    description: str
