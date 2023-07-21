from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from src.models.playlist import Playlist
from src.models.track import Track
from src.models.artist import Artist
from src.models.album import Album

load_dotenv()

scope = "playlist-read-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))


def get_spotify_playlists() -> list[Playlist]:
    response = sp.user_playlists("viktorbubanja")
    playlists = []
    for item in response["items"]:
        playlist = Playlist(name=item["name"], external_id=item["id"], image_url=item["images"][0]["url"])
        playlists.append(playlist)
    return playlists


def get_tracks_in_playlist(playlist_id: str) -> list[Track]:
    response_tracks = sp.playlist_items(playlist_id)["items"]

    track_ids = [track_info["track"]["id"] for track_info in response_tracks]
    audio_features_of_tracks = sp.audio_features(track_ids)

    artist_ids = [track_info["track"]["artists"][0]["id"] for track_info in response_tracks]
    artists = sp.artists(artist_ids)["artists"]

    tracks = []
    for response_track, artist_info, audio_features in zip(response_tracks, artists, audio_features_of_tracks):
        track_info = response_track["track"]
        artist = Artist(
            name=artist_info["name"],
            external_id=artist_info["id"],
            external_url=artist_info["external_urls"]["spotify"],
            image_url=artist_info["images"][0]["url"],
            genres=artist_info["genres"],
        )
        album = Album(
            name=track_info["album"]["name"],
            external_id=track_info["album"]["id"]
        )
        track = Track(
            external_id=track_info["id"],
            name=track_info["name"],
            artists=[artist],
            album=album,
            duration=int(track_info["duration_ms"] / 1000),
            **audio_features
        )
        tracks.append(track)
    return tracks
