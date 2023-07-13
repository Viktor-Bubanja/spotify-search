from src.utils.dynamodb import DynamoDB


def test_save_item():
    dynamodb = DynamoDB()
    item = {
        "id": "123",
        "name": "test",
        "artists": "test",
        "album": "test",
        "image": "test",
        "preview": "test",
        "external_url": "test",
        "popularity": 1,
    }
    response = dynamodb.save_item(item)
    assert response["ResponseMetadata"]["HTTPStatusCode"] == 200


def test_get_item():
    dynamodb = DynamoDB()
    item = {"id": "123"}
    response = dynamodb.get_item(item)
    assert response["ResponseMetadata"]["HTTPStatusCode"] == 200
    assert response["Item"]["id"] == "123"
