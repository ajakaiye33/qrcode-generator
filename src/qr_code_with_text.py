from PIL import Image, ImageDraw, ImageFont
import asyncio


class QRCodeWithText:
    def __init__(self, qr_img, text, font_path, font_size=15):
        self.qr_img = qr_img
        self.text = text
        self.font_path = font_path
        self.font_size = font_size

    def create_image_with_text(self):
        font = ImageFont.truetype(self.font_path, self.font_size)
        qr_with_text = Image.new(
            "RGB", (self.qr_img.size[0], self.qr_img.size[1] + 50), "white"
        )
        qr_with_text.paste(self.qr_img, (0, 0))
        draw = ImageDraw.Draw(qr_with_text)
        text_bbox = draw.textbbox((0, 0), self.text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        #text_height = text_bbox[3] - text_bbox[1]
        text_position = (
            (qr_with_text.size[0] - text_width) // 2,
            self.qr_img.size[1] + 10,
        )
        draw.text(text_position, self.text, fill="black", font=font)
        return qr_with_text

    async def save_image(self, qr_with_text, path):
        await asyncio.to_thread(qr_with_text.save, path, format="PNG")
