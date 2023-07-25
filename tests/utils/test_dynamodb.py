def test_save_item(dynamodb):
    item = {
        "PK": "123",
        "SK": "track",
        "name": "test",
        "artists": "test",
        "album": "test",
    }
    response = dynamodb.save_item(item)
    assert response["ResponseMetadata"]["HTTPStatusCode"] == 200
    assert dynamodb.get_item({"PK": "123", "SK": "track"})["Item"]["PK"] == "123"


def test_save_items(dynamodb):
    items = [
        {
            "PK": "123",
            "SK": "track",
            "name": "test",
            "artists": "test",
            "album": "test",
        },
        {
            "PK": "456",
            "SK": "track",
            "name": "test",
            "artists": "test",
            "album": "test",
        },
    ]
    dynamodb.save_items(items)
    assert dynamodb.get_item({"PK": "123", "SK": "track"})["Item"]["PK"] == "123"
    assert dynamodb.get_item({"PK": "456", "SK": "track"})["Item"]["PK"] == "456"


def test_get_item(dynamodb):
    pk = "123"
    response = dynamodb.get_item({"PK": pk, "SK": "track"})
    assert response["ResponseMetadata"]["HTTPStatusCode"] == 200
    assert response["Item"]["PK"] == pk
