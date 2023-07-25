from fastapi import FastAPI
from src.spotify import get_playlists as get_spotify_playlists, get_tracks_in_playlist
from src.dynamodb import DynamoDB
from src.dynamodb_mapper import track_to_dynamodb

app = FastAPI()


@app.get("/playlists")
def get_playlists():
    return get_spotify_playlists()


@app.get("/playlists/{playlist_id}")
def get_playlist(playlist_id: str):
    return get_tracks_in_playlist(playlist_id)


@app.post("/playlists/{playlist_id}/save")
def save_playlist(playlist_id: str):
    tracks = get_tracks_in_playlist(playlist_id)
    db_tracks = [track_to_dynamodb(track) for track in tracks]
    DynamoDB().save_items(db_tracks)
    return "success"