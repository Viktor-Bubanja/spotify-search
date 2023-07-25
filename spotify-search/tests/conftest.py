import boto3
import json
import os
import pytest
from opensearchpy import OpenSearch as OpenSearchPy
from src.utils.environment_variables import *

DIR_PATH = os.path.dirname(__file__)

from src.opensearch import OpenSearch, TRACKS_INDEX
from src.dynamodb import DynamoDB

@pytest.fixture(scope="session", autouse=True)
def setup_tracks_index(opensearch):
    index_mapping = os.path.join(DIR_PATH, f"../../index-management/definitions/dev/{TRACKS_INDEX}.json")
    f = open(index_mapping)
    data = json.load(f)
    opensearch.create_index(index=TRACKS_INDEX, body=data)
    yield
    opensearch.delete_index(TRACKS_INDEX)


@pytest.fixture(scope="session", autouse=True)
def setup_dynamodb_table(dynamodb):
    dynamodb.create_table(
        attribute_definitions=[
            {
                "AttributeName": "PK",
                "AttributeType": "S"
            },
            {
                "AttributeName": "SK",
                "AttributeType": "S"
            }
        ],
        key_schema=[
            {
                "AttributeName": "PK",
                "KeyType": "HASH"
            },
            {
                "AttributeName": "SK",
                "KeyType": "RANGE"
            }
        ],
    )
    yield
    dynamodb.delete_table()


@pytest.fixture(scope="session")
def dynamodb():
    client = boto3.resource("dynamodb", endpoint_url="http://localhost:8000")
    return DynamoDB(client=client)


@pytest.fixture(scope="session")
def opensearch():
    host, port = get_opensearch_host(), get_opensearch_port()
    username, password = get_username_password()

    client = OpenSearchPy(
        hosts=[{"host": host, "port": port}],
        http_auth=(username, password),
        use_ssl=True,
        verify_certs=False,
    )
    return OpenSearch(client)