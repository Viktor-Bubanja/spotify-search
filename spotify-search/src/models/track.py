from pydantic import BaseModel
from src.models.artist import Artist
from src.models.album import Album

class Track(BaseModel):
    external_id: str
    name: str
    artists: list[Artist]
    album: Album
    duration: int
    danceability: float
    energy: float
    key: int
    speechiness: float
    acousticness: float
    instrumentalness: float
    liveness: float
    valence: float
    tempo: float
    time_signature: int
    mode: int
