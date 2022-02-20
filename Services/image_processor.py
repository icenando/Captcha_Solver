from dataclasses import dataclass

from numpy import asarray, mean, ndarray
from PIL import Image, ImageOps
from scipy import ndimage

from ..Logger import get_logger

log = get_logger(__name__)


@dataclass
class Image_Processor:
    out_img: str
    avg_deviation: int
    u_filter: int

    def read_captcha(self, captcha_img: str) -> Image:
        log.info(f"Opening image: {captcha_img}")
        try:
            return Image.open(captcha_img)
        except Exception as e:
            raise SystemExit(f"Error opening image: {e}")

    def convert_img_to_monochrome(self, captcha_img: Image) -> Image:
        log.info(f"Converting image to greyscale.")
        try:
            return ImageOps.grayscale(captcha_img)
        except Exception as e:
            raise SystemExit(f"Error converting image to grayscale: {e}")

    def convert_img_to_array(self, input_img: Image) -> ndarray:
        log.info("Converting image to ndarray.")
        try:
            input_img.verify()
            return asarray(input_img)
        except Exception as e:
            raise SystemExit(f"Error converting image to ndarray: {e}")

    def increase_constrast(self, in_file: ndarray) -> ndarray:
        log.info("Increasing contrast.")
        try:
            assert type(in_file) == ndarray
            avg = mean(in_file, axis=(0, 1))
        except Exception as e:
            raise SystemExit(
                f"Failed to get mean. The ndarray dimensions might be wrong, or the object is not of type ndarray: {e}"
            )
        log.info("Changing pixel values.")
        for i, row in enumerate(in_file):
            for pixel, value in enumerate(row):
                # If pixel value is higher than the average of the image,
                # it is changed to white, otherwise to black.
                if value <= avg + self.avg_deviation:
                    in_file[i][pixel] = 0
                else:
                    in_file[i][pixel] = 255
        return in_file

    def neighbour_comparison(self, in_file: ndarray) -> ndarray:
        # Fills in central pixel with the same colour as its neighbouring pixels.
        # The number is neighbouring pixels to compare agains is defined by "u_filter"
        log.info("Changing pixels based on their neighbours' brightness values.")
        try:
            assert type(in_file) == ndarray
            return ndimage.uniform_filter(
                in_file, self.u_filter, mode="constant", cval=0
            )
        except Exception as e:
            raise SystemExit(
                f"Failed to apply neighbour_comparison.uniform_filter: {e}"
            )

    def invert_colours(self, img: Image) -> Image:
        try:
            log.info("Inverting colours.")
            img.verify()
            return ImageOps.invert(img)
        except Exception as e:
            raise SystemExit(f"Invalid image: {e}")

    def save_image(self, out_file: Image) -> None:
        log.info(f"Saving file.")
        try:
            out_file.verify()
            out_file.save(self.out_img)
        except Exception as e:
            raise SystemExit(f"Failed to save outfile: {e}")
