from fastapi import FastAPI
from src.spotify import get_spotify_playlists

app = FastAPI()


@app.get("/playlists")
def get_playlists():
    return get_spotify_playlists()


@app.get("/playlists/{playlist_id}")
def get_playlist(playlist_id: str):
    return ""
