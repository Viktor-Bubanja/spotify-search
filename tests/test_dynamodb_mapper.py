from src.dynamodb_mapper import track_to_dynamodb
from src.models.track import Track
from src.models.album import Album
from src.models.artist import Artist

def test_track_to_dynamodb():
    track = Track(
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
    )
    dynamodb_item = track_to_dynamodb(track)
    expected_dynamodb_item = {
        "PK": "05PeuyOcr9GzSv8PmPwCSx",
        "SK": "track",
        "body": {
            "external_id": "05PeuyOcr9GzSv8PmPwCSx",
            "name": "Verschwende deine Zeit",
            "artists": [
                {
                    "name": "Edwin Rosen",
                    "genres": [
                        "neue neue deutsche welle"
                    ],
                    "external_id": "1r93D0anfnfL4M7tYTce0J",
                    "external_url": "https://open.spotify.com/artist/1r93D0anfnfL4M7tYTce0J",
                    "image_url": "https://i.scdn.co/image/ab6761610000e5ebf0e689fd2ae90078ead32776"
                }
            ],
            "album": {
                "name": "Verschwende deine Zeit"
            },
            "duration": 158,
            "danceability": 0.501,
            "energy": 0.843,
            "key": 0,
            "speechiness": 0.0417,
            "acousticness": 0.862,
            "instrumentalness": 0.0089,
            "liveness": 0.12,
            "valence": 0.542,
            "tempo": 181.823,
            "time_signature": 4,
            "mode": 1
        },
    }
    assert dynamodb_item == expected_dynamodb_item