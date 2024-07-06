import asyncio
import os
from utils.file_utils import load_config
from src.qr_code_generator import QRCodeGenerator
from src.qr_code_with_text import QRCodeWithText
from loguru import logger


async def generate_qr_code(data, text, logo_path, font_path, output_path):
    # Generate QR code
    qr_generator = QRCodeGenerator(data)
    qr_generator.add_logo(logo_path)
    await qr_generator.save_image(output_path)

    # Create QR code with text
    qr_with_text_creator = QRCodeWithText(qr_generator.img, text, font_path)
    qr_with_text_img = qr_with_text_creator.create_image_with_text()
    await qr_with_text_creator.save_image(qr_with_text_img, output_path)


async def main():
    # Load configuration
    config = load_config("config/config.json")

    urls_and_texts = config["urls_and_texts"]
    logo_path = config["logo_path"]
    font_path = config["font_path"]
    output_dir = config["output_dir"]

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Generate QR codes
    tasks = []
    for idx, entry in enumerate(urls_and_texts):
        output_path = os.path.join(
            output_dir, f"social_media_profile_qrcode_with_text_{idx+1}.png"
        )
        tasks.append(
            generate_qr_code(
                entry["url"], entry["text"], logo_path, font_path, output_path
            )
        )

    await asyncio.gather(*tasks)

    logger.info(f"Generated {len(urls_and_texts)} QR Codes with text.")


# Run the main function
if __name__ == "__main__":
    asyncio.run(main())
