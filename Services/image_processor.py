from dataclasses import dataclass
from numpy import asarray, mean, ndarray
from PIL import Image, ImageOps
from scipy import ndimage

@dataclass
class Image_Processor:
    out_img: str
    avg_deviation: int
    u_filter: int
    
    
    def read_captcha(self, captcha_img: str) -> Image:
        return Image.open(captcha_img)
        
    def convert_img_to_monochrome(self, captcha_img: Image) -> Image:
        return ImageOps.grayscale(captcha_img)
    
    def convert_img_to_array(self, input_img: Image) -> ndarray:
        return asarray(input_img)


    def increase_constrast(self, in_file: ndarray) -> ndarray:
        
        avg = mean(in_file, axis=(0, 1))
        
        for i, row in enumerate(in_file):
            for pixel, value in enumerate(row):
                # If pixel value is higher than the average of the image, 
                # transforms to white, otherwise black.
                if value <= avg + self.avg_deviation:
                    in_file[i][pixel] = 0
                else:
                    in_file[i][pixel] = 255
                    
        return in_file


    def neighbour_comparison(self, in_file: ndarray) -> ndarray:
        # Fills in central pixel with thhe same colour as its neighbouring pixels. 
        # The number is neighbouring pixels to compare agains is defined by "u_filter"
        return ndimage.uniform_filter(in_file, self.u_filter, mode="constant", cval=0)
    
    def invert_colours(self, img: Image) -> Image:
        return ImageOps.invert(img)
    
    def save_image(self, out_file: Image) -> None:
        out_file.save(self.out_img)
        out_file.close()