from pydantic import BaseModel


class City(BaseModel):
    uid: int
    name: str


class Route(BaseModel):
    uid: int
    name: str
    city_id: int


class Place(BaseModel):
    name: str
