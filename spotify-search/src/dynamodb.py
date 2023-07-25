import boto3
from functools import cache

SPOTIFY_SEARCH_TABLE = "spotify-search"

@cache
def _dynamodb_client():
    return boto3.resource("dynamodb")


# This class implements a Single-Table design so does not allow for the table variable to be changed
class DynamoDB:
    def __init__(self, client = None):
        if client is None:
            client = _dynamodb_client()
        self.client = client
        self.table = self.client.Table(SPOTIFY_SEARCH_TABLE)

    def save_item(self, item: dict) -> dict:
        return self.table.put_item(Item=item)

    def save_items(self, items: list[dict]) -> dict:
        with self.table.batch_writer() as batch:
            for item in items:
                batch.put_item(Item=item)

    def get_item(self, item: dict) -> dict:
        return self.table.get_item(Key=item)

    def create_table(self, key_schema: list, attribute_definitions: list) -> dict:
        return self.client.create_table(
            TableName=SPOTIFY_SEARCH_TABLE,
            KeySchema=key_schema,
            AttributeDefinitions=attribute_definitions,
            BillingMode="PAY_PER_REQUEST",
        )

    def delete_table(self) -> dict:
        return self.table.delete()
