import pytest
from utils.file_utils import load_config


@pytest.fixture
def setup():
    config_path = "config/config.json"
    return load_config(config_path)
