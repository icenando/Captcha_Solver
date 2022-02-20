from os import path
from platform import processor

import pytest
from numpy import isin
from Services.image_processor import Image_Processor
from Services.text_extraction import Text_Extraction


class TestTextExtraction:
    image_processor = Image_Processor("", 1, 1)
    captcha_img = path.join("Resources", "in", "2646.jpeg")
    expected_result = path.join(path.basename(captcha_img)).split('.')[0] + '\n'
    text_extraction = Text_Extraction(image_processor)
    
    def test_text_extraction_raises_exception(self):
        with pytest.raises(SystemExit):
            self.text_extraction.extract_text("")
            
    def test_text_extraction_returns_string(self):
        try:
            result = self.text_extraction.extract_text(self.captcha_img)
            assert isinstance(result, str)
        except:
            pytest.fail()

