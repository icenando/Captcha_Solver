from numpy import asarray, mean, ndarray
from PIL import Image, ImageOps
from scipy import ndimage

### TWEEK THESE ###
captcha_file = "3.jpeg"
avg_deviation = 40
u_filter = 3
###################

def increase_constrast(in_file: ndarray) -> ndarray:
    avg = mean(in_file, axis=(0, 1))
    for i, row in enumerate(in_file):
        for pixel, value in enumerate(row):
            if value <= avg + avg_deviation:
                in_file[i][pixel] = 0
            else:
                in_file[i][pixel] = 255
    return in_file

def neighbour_comparison(in_file):
    return ndimage.uniform_filter(in_file, u_filter, mode="constant", cval=0)

in_file = asarray(ImageOps.grayscale(Image.open(captcha_file)))

out_file = Image.fromarray(increase_constrast(in_file))
in_file = neighbour_comparison(in_file)
in_file = neighbour_comparison(in_file)
out_file = Image.fromarray(increase_constrast(in_file))

out_file = ImageOps.invert(out_file)

out_file.show()
