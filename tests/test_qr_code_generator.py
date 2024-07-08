import os
import pytest
from src.qr_code_generator import QRCodeGenerator


@pytest.fixture(name="setup")
def sample_data():
    return "https://x.com/barackobama/"


@pytest.fixture(name="setup")
def logo_path():
    return "./image/github.png"


@pytest.fixture(name="setup")
def output_path(tmpdir):
    return os.path.join(tmpdir, "qr_code.png")


@pytest.mark.asyncio
async def test_qr_code_generation(sample_data, output_path):
    qr_generator = QRCodeGenerator(sample_data)
    await qr_generator.save_image(output_path)
    assert os.path.exists(output_path)


@pytest.mark.asyncio
async def test_add_logo(sample_data, logo_path, output_path):
    qr_generator = QRCodeGenerator(sample_data)
    qr_generator.add_logo(logo_path)
    await qr_generator.save_image(output_path)
    assert os.path.exists(output_path)
