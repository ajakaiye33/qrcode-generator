import os
import pytest
from utils.file_utils import load_config


@pytest.fixture
def config_path():
    return "config/config.json"


def test_load_config(config_path):
    config = load_config(config_path)
    assert "urls_and_texts" in config
    assert "logo_path" in config
    assert "font_path" in config
    assert "output_dir" in config
