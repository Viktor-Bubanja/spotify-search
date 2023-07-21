import pytest
from src.spotify import get_playlists, get_tracks_in_playlist
from src.models.playlist import Playlist
from src.models.track import Track
from src.models.album import Album
from src.models.artist import Artist
from tests.fixtures.spotify.user_playlists_response import response as user_playlists_response
from tests.fixtures.spotify.playlist_items_response import response as playlist_items_response
from tests.fixtures.spotify.audio_features_response import response as audio_features_response
from tests.fixtures.spotify.artists_response import response as artists_response


@pytest.fixture
def mock_user_playlists(mocker):
    return mocker.patch(
        "src.spotify.spotipy.Spotify.user_playlists",
        return_value=user_playlists_response
    )

@pytest.fixture
def mock_playlist_items(mocker):
    return mocker.patch(
        "src.spotify.spotipy.Spotify.playlist_items",
        return_value=playlist_items_response
    )

@pytest.fixture
def mock_audio_features(mocker):
    return mocker.patch(
        "src.spotify.spotipy.Spotify.audio_features",
        return_value=audio_features_response
    )

@pytest.fixture
def mock_artists(mocker):
    return mocker.patch(
        "src.spotify.spotipy.Spotify.artists",
        return_value=artists_response
    )


def test_get_playlists(mock_user_playlists):
    playlists = get_playlists()
    expected_playlists = [
        Playlist(name='slappers', external_id='7y1BrGaP2GuK1EyMEvzzuQ', image_url='https://i.scdn.co/image/ab67616d0000b273fc3f8866faf5d09164a0e555'),
        Playlist(name='bangersbangersbangers', external_id='2gJeH2CmAIMnPG06ebrCx5', image_url='https://i.scdn.co/image/ab67616d0000b27376426e7040d397700d3c123c'),
    ]
    assert playlists == expected_playlists

def test_get_tracks_in_playlist(mock_playlist_items, mock_audio_features, mock_artists):
    tracks = get_tracks_in_playlist("7y1BrGaP2GuK1EyMEvzzuQ")
    expected_tracks = [
        Track(
            external_id='05PeuyOcr9GzSv8PmPwCSx',
            name='Verschwende deine Zeit',
            artists=[
                Artist(
                    name='Edwin Rosen',
                    genres=['neue neue deutsche welle'],
                    external_id='1r93D0anfnfL4M7tYTce0J',
                    external_url='https://open.spotify.com/artist/1r93D0anfnfL4M7tYTce0J',
                    image_url='https://i.scdn.co/image/ab6761610000e5ebf0e689fd2ae90078ead32776'
                )
            ],
            album=Album(
                name='Verschwende deine Zeit'
            ),
            duration=158,
            danceability=0.501,
            energy=0.843,
            key=0,
            speechiness=0.0417,
            acousticness=0.862,
            instrumentalness=0.0089,
            liveness=0.12,
            valence=0.542,
            tempo=181.823,
            time_signature=4,
            mode=1
        ),
        Track(
            external_id='12zbxFV5Z6rJk9aoHOXz2s',
            name='shameless',
            artists=[
                Artist(
                    name='Nilüfer Yanya',
                    genres=['art pop', 'uk alternative pop'],
                    external_id='09kXLeOXRyfNQMXRaDO4qA',
                    external_url='https://open.spotify.com/artist/09kXLeOXRyfNQMXRaDO4qA',
                    image_url='https://i.scdn.co/image/ab6761610000e5eb1772815fafe2bdda56ce532d'
                )
            ],
            album=Album(name='PAINLESS'),
            duration=274,
            danceability=0.768,
            energy=0.434,
            key=4,
            speechiness=0.0309,
            acousticness=0.287,
            instrumentalness=8.11e-05,
            liveness=0.115,
            valence=0.602,
            tempo=120.017,
            time_signature=4,
            mode=1
        ),
    ]
    assert tracks == expected_tracks