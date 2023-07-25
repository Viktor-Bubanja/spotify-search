import os
from functools import cache
from src.utils.environment_variables import *

from opensearchpy import OpenSearch as OpenSearchPy

TRACKS_INDEX = "tracks"


@cache
def _opensearch_client():
    host, port = get_opensearch_host(), 443
    username, password = get_username_password()

    return OpenSearchPy(
        hosts=[{"host": host, "port": port}],
        http_auth=(username, password),
        use_ssl=True,
        verify_certs=True,
    )

class OpenSearch:
    def __init__(self, client = None):
        if client is None:
            client = _opensearch_client()
        self.client = client

    def search(self, index: str, query: dict) -> dict:
        return self.client.search(index=index, body=query)

    def index(self, index: str, body: dict) -> dict:
        return self.client.index(index=index, body=body)

    def create_index(self, index: str, body: dict) -> dict:
        return self.client.indices.create(index=index, body=body)

    def delete_index(self, index: str) -> dict:
        return self.client.indices.delete(index)
