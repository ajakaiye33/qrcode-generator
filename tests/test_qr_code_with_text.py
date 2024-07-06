import os
import pytest
from PIL import Image
from qr.qr_code_with_text import QRCodeWithText


@pytest.fixture
def sample_image():
    return Image.new("RGB", (200, 200), "white")


@pytest.fixture
def sample_text():
    return "Test Text"


@pytest.fixture
def font_path():
    return "path/to/your/font.ttf"


@pytest.fixture
def output_path(tmpdir):
    return os.path.join(tmpdir, "qr_code_with_text.png")


@pytest.mark.asyncio
async def test_add_text(sample_image, sample_text, font_path, output_path):
    qr_with_text_creator = QRCodeWithText(sample_image, sample_text, font_path)
    qr_with_text_img = qr_with_text_creator.create_image_with_text()
    await qr_with_text_creator.save_image(qr_with_text_img, output_path)
    assert os.path.exists(output_path)
