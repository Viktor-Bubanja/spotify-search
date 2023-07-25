import requests


BASE_URL = "http://127.0.0.1:8000"


def test_get_playlist():
    response = requests.get(BASE_URL + "/playlists/1")
    expected_status_code = 200
    expected_body = ""
    assert response.status_code == expected_status_code
    assert response.json() == expected_body
