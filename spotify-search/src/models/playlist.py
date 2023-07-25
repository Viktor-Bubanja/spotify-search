from pydantic import BaseModel

class Playlist(BaseModel):
    name: str
    external_id: str
    image_url: str
