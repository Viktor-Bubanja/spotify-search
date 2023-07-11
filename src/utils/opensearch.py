import os
from functools import cache
from typing import Any
from src.utils.environment_variables import dev_env, get_username_password

from opensearchpy import OpenSearch

TRACKS_INDEX = "tracks"


@cache
def _opensearch_client():
    host = os.environ.get("OPENSEARCH_HOST")
    username, password = get_username_password()
    if not dev_env():
        port = 443
        verify_certs = True
    else:
        port = os.environ.get("OPENSEARCH_PORT")
        verify_certs = False

    return OpenSearch(
        hosts=[{"host": host, "port": port}],
        http_auth=(username, password),
        use_ssl=True,
        verify_certs=verify_certs,
    )


def search(index, query):
    return _opensearch_client().search(index=index, body=query)


def index(index, body):
    return _opensearch_client().index(index=index, body=body)


def create_index(index: str, body: Any) -> dict:
    return _opensearch_client().indices.create(index=index, body=body)


def delete_index(index: str) -> dict:
    return _opensearch_client().indices.delete(index)
