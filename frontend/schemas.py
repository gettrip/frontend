from pydantic import BaseModel


class City(BaseModel):
    uid: int
    name: str


class Route(BaseModel):
    name: str
