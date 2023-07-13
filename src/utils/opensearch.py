import os
from functools import cache
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

class OpenSearch:
    def __init__(self, client=_opensearch_client()):
        self.client = client

    def search(self, index: str, query: dict) -> dict:
        return self.client.search(index=index, body=query)

    def index(self, index: str, body: dict) -> dict:
        return self.client.index(index=index, body=body)

    def create_index(self, index: str, body: dict) -> dict:
        return self.client.indices.create(index=index, body=body)

    def delete_index(self, index: str) -> dict:
        return self.client.indices.delete(index)
