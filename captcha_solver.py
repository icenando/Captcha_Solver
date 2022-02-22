#!python3

# Entry point to captcha solver. Takes filename and returns extracted text as str.

from os import path

from PIL import Image

import Logger
from Services.image_processor import Image_Processor
from Services.text_extraction import Text_Extraction

##################### TWEEK THis #####################
file_name = "2646.jpeg"
#
# OPTIONAL CHANGES - LEAVE AS IS FOR STANDARD PROCESSING
avg_deviation = 20
u_filter = 4
captcha_text_length = 4
#######################################################

captcha_img_file = path.join("Resources", "in", file_name)
out_img = path.join("Resources", "out", path.basename(captcha_img_file))

log = Logger.get_logger(__name__)

def main(captcha_img: str, out_img: str) -> str:
    
    global avg_deviation
    global u_filter
    
    text = ''
    best_match = ''
    max_tries = avg_deviation
    
    while len(text) != captcha_text_length and max_tries > 0:
        
        print(f"Attempts remaining #{max_tries}", end='\t')
        
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

            text = text_extractor.extract_text(out_img).split('\n')[0]
            print(f"Extracted text: {text}\n")
            
            if len(text) == captcha_text_length:
                return text
            else:
                max_tries -= 1
                avg_deviation += 1
                if len(text) > len(best_match) and len(text) < (captcha_text_length+1):
                    best_match = text  
                else: continue

        except Exception as e:
            log.error(e)
            SystemExit()
            break
        
    print(f"Best match: {best_match}\n")    
    return best_match

if __name__ == "__main__":
    main(captcha_img_file, out_img)
