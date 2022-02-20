from os import path

from PIL import Image

import Logger
from Services.image_processor import Image_Processor
from Services.text_extraction import Text_Extraction

##################### TWEEK THESE #####################
captcha_img_file = path.join("Resources", "in", "2646.jpeg")
out_img = path.join("Resources", "out", path.basename(captcha_img_file))
avg_deviation = 30
u_filter = 4
#######################################################

log = Logger.get_logger(__name__)

def main(captcha_img):
    try:
        image_processor = Image_Processor(out_img, avg_deviation, u_filter)
        text_extractor = Text_Extraction(image_processor)

        in_file = image_processor.convert_img_to_array(
            image_processor.convert_img_to_monochrome(
                image_processor.read_captcha(captcha_img)
            )
        )

        out_file = Image.fromarray(image_processor.increase_constrast(in_file))
        in_file = image_processor.neighbour_comparison(in_file)
        in_file = image_processor.neighbour_comparison(in_file)
        out_file = Image.fromarray(image_processor.increase_constrast(in_file))

        out_file = image_processor.invert_colours(out_file)

        image_processor.save_image(out_file)

        text = text_extractor.extract_text(out_img)
        print(f"\nExtracted text: {text}\n")
        
        return text

    except Exception as e:
        log.error(e)
        SystemExit()

if __name__ == "__main__":
    main(captcha_img=captcha_img_file)
