from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

scope = "playlist-read-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

tracks = sp.playlist_tracks("0QLtG6JsXNQhwh4BKKv8A7")
for track_info in tracks["items"]:
    track = track_info["track"]
    print(f"Song: {track['name']}")
    print(f"Artist: {track['artists'][0]['name']}")