from os import path

import pytest
from numpy import asarray, logical_and, ndarray
from PIL import Image, ImageOps

from Services.image_processor import Image_Processor


class TestImageProcessor:
    processor = Image_Processor("", 1, 1)
    avg_deviation = 35
    captcha_img = path.join("Resources", "in", "3.jpeg")
    image = Image.open(captcha_img)
    monochrome_image = ImageOps.grayscale(image)
    ndarray_image = asarray(monochrome_image)

    def test_read_captcha_raises_exception(self):
        with pytest.raises(SystemExit):
            self.processor.read_captcha("")

    def test_read_captcha_returns_correct_image_object(self):
        try:
            image = Image.open(self.captcha_img)
            assert image == self.processor.read_captcha(self.captcha_img)
        except:
            pytest.fail()

    def test_convert_img_to_monochrome_raises_exception(self):
        with pytest.raises(SystemExit):
            self.processor.convert_img_to_monochrome("")

    def test_convert_img_to_monochrome_returns_monochrome_image_object(self):
        try:
            assert self.monochrome_image == self.processor.convert_img_to_monochrome(
                self.image
            )
        except:
            pytest.fail()

    def test_convert_img_to_array_raises_exception(self):
        with pytest.raises(SystemExit):
            self.processor.convert_img_to_array("")

    def test_convert_img_to_array_returns_correct_ndarray(self):
        try:
            assert (
                logical_and(
                    self.ndarray_image,
                    self.processor.convert_img_to_array(self.monochrome_image),
                )
            ).all()
        except:
            pytest.fail()

    def test_increase_constrast_raises_exception(self):
        with pytest.raises(SystemExit):
            self.processor.increase_constrast("")

    def test_increase_constrast_returns_an_ndarray(self):
        try:
            assert isinstance(
                self.processor.increase_constrast(self.ndarray_image), ndarray
            )
        except:
            pytest.fail()

    def test_neighbour_comparison_raises_exception(self):
        with pytest.raises(SystemExit):
            self.processor.neighbour_comparison("")

    def test_neighbour_comparison_returns_an_ndarray(self):
        try:
            assert isinstance(
                self.processor.neighbour_comparison(self.ndarray_image), ndarray
            )
        except:
            pytest.fail()

    def test_invert_colours_raises_exception(self):
        with pytest.raises(SystemExit):
            self.processor.invert_colours("")

    def test_invert_colours_returns_image_object(self):
        try:
            inverted_img = self.processor.invert_colours(self.monochrome_image)
            assert isinstance(inverted_img, Image.Image)
        except:
            pytest.fail()

    def testsave_image_raises_exception(self):
        with pytest.raises(SystemExit):
            self.processor.save_image("")
