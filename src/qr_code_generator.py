import qrcode
from PIL import Image
import asyncio
from loguru import logger


class QRCodeGenerator:
    def __init__(self, data, box_size=5, border=4):
        self.qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=box_size,
            border=border,
        )
        self.qr.add_data(data)
        self.qr.make(fit=True)
        self.img = self.qr.make_image(fill_color="black", back_color="white").convert(
            "RGBA"
        )

    def add_logo(self, logo_path, base_width=100):
        try:
            logo_display = Image.open(logo_path).convert("RGBA")
            wpercent = base_width / float(logo_display.size[0])
            hsize = int((float(logo_display.size[1]) * float(wpercent)))
            logo_display = logo_display.resize((base_width, hsize))

            pos = (
                (self.img.size[0] - logo_display.size[0]) // 2,
                (self.img.size[1] - logo_display.size[1]) // 2,
            )

            # Create a new image with the same size as the QR code image and transparent background
            new_img = Image.new("RGBA", self.img.size)
            new_img.paste(self.img, (0, 0))
            new_img.paste(logo_display, pos, mask=logo_display)

            self.img = new_img
        except FileNotFoundError:
            logger.error(f"Logo file '{logo_path}' not found. Proceeding without logo.")

    async def save_image(self, path):
        await asyncio.to_thread(self.img.save, path, format="PNG",compress_level=9)
