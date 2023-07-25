from src.models.track import Track

def track_to_dynamodb(track: Track) -> dict:
    return {
        "PK": track.external_id,
        "SK": "track",
        "body": track.model_dump_json(),
    }