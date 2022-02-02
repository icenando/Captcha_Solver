from dataclasses import dataclass
from numpy import asarray, mean, ndarray
from PIL import Image, ImageOps
from scipy import ndimage
from os import path

##################### TWEEK THESE #####################
captcha_img = "in/3.jpeg"
out_img = path.join("out", path.basename(captcha_img))
avg_deviation = 40
u_filter = 3
#######################################################

@dataclass
class Image_Processor:
    
    def read_captcha(self, captcha_img):
        return Image.open(captcha_img)
        
    def convert_img_to_monochrome(self, captcha_img):
        return ImageOps.grayscale(captcha_img)
    
    def convert_img_to_array(self, input_img):
        return asarray(input_img)


    def increase_constrast(self, in_file: ndarray) -> ndarray:
        
        avg = mean(in_file, axis=(0, 1))
        
        for i, row in enumerate(in_file):
            for pixel, value in enumerate(row):
                # If pixel value is higher than the average of the image, 
                # transforms to white, otherwise black.
                if value <= avg + avg_deviation:
                    in_file[i][pixel] = 0
                else:
                    in_file[i][pixel] = 255
                    
        return in_file


    def neighbour_comparison(self, in_file: ndarray) -> ndarray:
        # Fills in central pixel with thhe same colour as its neighbouring pixels. 
        # The number is neighbouring pixels to compare agains is defined by "u_filter"
        return ndimage.uniform_filter(in_file, u_filter, mode="constant", cval=0)
    
    def invert_colours(self, img: Image) -> Image:
        return ImageOps.invert(img)
    
    
    def save_image(self, out_file: Image) -> None:
        out_file.save(out_img)
        out_file.close()
        
    
if __name__=="__main__":
    
    image_processor = Image_Processor()

    in_file = image_processor.convert_img_to_array(
            image_processor.convert_img_to_monochrome(
            image_processor.read_captcha(captcha_img)
            ))

    out_file = Image.fromarray(image_processor.increase_constrast(in_file))
    in_file = image_processor.neighbour_comparison(in_file)
    in_file = image_processor.neighbour_comparison(in_file)
    out_file = Image.fromarray(image_processor.increase_constrast(in_file))

    out_file = image_processor.invert_colours(out_file)

    image_processor.save_image(out_file)
    


