import pytest
import requests
from src.models.playlist import Playlist


BASE_URL = "http://127.0.0.1:8000"

@pytest.fixture
def mock_get_spotify_playlists(mocker):
    return mocker.patch(
        "src.api.get_spotify_playlists",
        return_value=[
            Playlist(name='slappers', external_id='7y1BrGaP2GuK1EyMEvzzuQ', image_url='https://i.scdn.co/image/ab67616d0000b273fc3f8866faf5d09164a0e555'),
            Playlist(name='bangersbangersbangers', external_id='2gJeH2CmAIMnPG06ebrCx5', image_url='https://i.scdn.co/image/ab67616d0000b27376426e7040d397700d3c123c'),
        ]
    )

def test_get_playlists(mock_get_spotify_playlists):
    response = requests.get(BASE_URL + "/playlists")
    expected_status_code = 200
    expected_body = ""
    assert response.status_code == expected_status_code
    assert response.json() == expected_body


def test_get_playlist():
    response = requests.get(BASE_URL + "/playlists/1")
    expected_status_code = 200
    expected_body = ""
    assert response.status_code == expected_status_code
    assert response.json() == expected_body
