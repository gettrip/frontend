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
    duration: int


class Place(BaseModel):
    name: str
    image: str
    description: str
    duration: int


class RoutePoint(BaseModel):
    position: int
    distance: int
    place: Place
