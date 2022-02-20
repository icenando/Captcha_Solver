#!python3

# Uses Pytesseract to extract text from "clean" file.

from dataclasses import dataclass

import Logger
from pytesseract import pytesseract

from Services.image_processor import Image_Processor

log = Logger.get_logger(__name__)


@dataclass
class Text_Extraction:
    image_processor: Image_Processor

    def extract_text(self, clean_img: str) -> str:
        log.info(f"Extracting text from {clean_img}")
        try:
            captcha = self.image_processor.read_captcha(clean_img)
            return pytesseract.image_to_string(
                captcha, config="--psm 13 --oem 3 -c tessedit_char_whitelist=0123456789"
            )
        except Exception as e:
            log.error("An error ocurred when recognisint the text")
            raise SystemExit(f"An error ocurred when recognisint the text: {e}")
