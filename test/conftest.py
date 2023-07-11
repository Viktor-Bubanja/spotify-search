import json
import os
import pytest
from src.utils.opensearch import create_index, delete_index, TRACKS_INDEX
import dotenv


dotenv.load_dotenv('.env.test')
DIR_PATH = os.path.dirname(__file__)


@pytest.fixture(scope="session", autouse=True)
def setup_index():
    index_mapping = os.path.join(DIR_PATH, f"../index-management/definitions/dev/{TRACKS_INDEX}.json")
    f = open(index_mapping)
    data = json.load(f)
    create_index(index=TRACKS_INDEX, body=data)
    yield
    delete_index(TRACKS_INDEX)
