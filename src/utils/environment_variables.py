from typing import Optional
import os


def get_root_stage() -> Optional[str]:
    return os.getenv("ROOT_STAGE")


def dev_env() -> bool:
    return get_root_stage() == "dev"


def get_username_password() -> tuple[str, str]:
    username = os.getenv("OPENSEARCH_USER")
    password = os.getenv("OPENSEARCH_PASSWORD")
    return username, password
