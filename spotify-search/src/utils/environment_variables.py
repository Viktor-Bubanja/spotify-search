from typing import Optional
import os


def get_username_password() -> tuple[str, str]:
    username = os.getenv("OPENSEARCH_USER")
    password = os.getenv("OPENSEARCH_PASSWORD")
    return username, password


def get_opensearch_host() -> Optional[str]:
    return os.getenv("OPENSEARCH_HOST")


def get_opensearch_port() -> Optional[str]:
    return os.getenv("OPENSEARCH_PORT")