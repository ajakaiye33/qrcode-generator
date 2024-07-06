import argparse
import json
import os
import qrcode
import asyncio
from PIL import Image
from utils.file_utils import load_config
from src.qr_code_with_text import QRCodeWithText


def create_qr_code(url, box_size=10, border=4, fill_color="black", back_color="white"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=box_size,
        border=border,
    )
    qr.add_data(url)
    qr.make(fit=True)
    return qr.make_image(fill_color=fill_color, back_color=back_color)


def add_logo_to_qr(qr_img, logo_path):
    logo_display = Image.open(logo_path)
    base_width = 100
    wpercent = base_width / float(logo_display.size[0])
    hsize = int((float(logo_display.size[1]) * float(wpercent)))
    logo_display = logo_display.resize((base_width, hsize), Image.LANCZOS)
    pos = (
        (qr_img.size[0] - logo_display.size[0]) // 2,
        (qr_img.size[1] - logo_display.size[1]) // 2,
    )
    qr_img.paste(logo_display, pos, mask=logo_display)
    return qr_img


async def generate_qr_code(entry, logo_path, font_path, output_dir, with_text):
    url = entry["url"]
    text = entry.get("text", "")

    qr_img = create_qr_code(url)
    if logo_path:
        qr_img = add_logo_to_qr(qr_img, logo_path)

    if with_text and text:
        qr_with_text = QRCodeWithText(qr_img, text, font_path).create_image_with_text()
        output_path = os.path.join(output_dir, f"{text.replace(' ', '_')}.png")
        await QRCodeWithText(qr_img, text, font_path).save_image(
            qr_with_text, output_path
        )
    else:
        output_path = os.path.join(
            output_dir, f"{text.replace(' ', '_') or 'qr_code'}.png"
        )
        qr_img.save(output_path)
    print(f"QR Code generated and saved ")


async def main(config_path, output_dir, with_text):
    config = load_config(config_path)
    logo_path = config.get("logo_path")
    font_path = config.get("font_path")

    os.makedirs(output_dir, exist_ok=True)

    tasks = [
        generate_qr_code(entry, logo_path, font_path, output_dir, with_text)
        for entry in config["urls_and_texts"]
    ]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate QR Codes with optional logos and text."
    )
    parser.add_argument(
        "--config", type=str, required=True, help="Path to the configuration file."
    )
    parser.add_argument(
        "--output",
        type=str,
        default="./output",
        help="Directory to save the generated QR codes.",
    )
    parser.add_argument(
        "--with-text", action="store_true", help="Generate QR codes with text."
    )

    args = parser.parse_args()

    asyncio.run(main(args.config, args.output, args.with_text))
