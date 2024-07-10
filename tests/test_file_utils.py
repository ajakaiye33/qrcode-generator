import pytest
from utils.file_utils import load_config


@pytest.fixture
def setup():
    config_path = "config/config.json"
    return load_config(config_path)


def test_load_config(setup):
    config = setup
    assert "urls_and_texts" in config
    assert "logo_path" in config
    assert "font_path" in config
    assert "output_dir" in config
