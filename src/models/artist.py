from pydantic import BaseModel

class Artist(BaseModel):
    name: str
    genres: list[str]
    external_id: str
    external_url: str
    image_url: str