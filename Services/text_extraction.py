from dataclasses import dataclass

from pytesseract import pytesseract

from Services.image_processor import Image_Processor


@dataclass
class Text_Extraction:
    image_processor: Image_Processor

    def extract_text(self, clean_img: str) -> str:
        captcha = self.image_processor.read_captcha(clean_img)
        captcha.show()
        return pytesseract.image_to_string(
            captcha, config="--psm 13 --oem 3 -c tessedit_char_whitelist=0123456789"
        )
