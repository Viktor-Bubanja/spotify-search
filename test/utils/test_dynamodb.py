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


def test_get_item(dynamodb):
    pk = "123"
    response = dynamodb.get_item({"PK": pk, "SK": "track"})
    assert response["ResponseMetadata"]["HTTPStatusCode"] == 200
    assert response["Item"]["PK"] == pk
