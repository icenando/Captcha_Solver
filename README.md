**DESCRITION**

A simple captcha breaker. It has been tested with only one type of numeric captcha image (found in the "Resources > in" folder. It extracts a 4-digits long string from an image using [Pytesseract](https://pypi.org/project/pytesseract/).


**INSTALLATION**

1) [Install Tesseract](https://tesseract-ocr.github.io/tessdoc/Installation.html).
2) Download code.
3) Create a virtual environment and activate it.
4) `pip install -r requirements.txt`


**USAGE**

1) place captcha image in any[format accepted by Pillow](https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#fully-supported-formats) in "Resources > in".
2) In the root folder, open "captcha_solver.py" and change the "file_name" to the name of the captcha image uploaded in step 1.
3) Run it!
4) The function returns a 4-digit long string.


**OTHER SETTINGS**

1) captcha_solver.py

   1) `avg_deviation`: in order to reach absolute contrast, each pixel is compared with the average brightness of the whole image. If it's lower or equal than the sum of average and the user-defined avg_deviation, then the pixel is converted to pure black(pixel value of zero). Otherwise, it's converted to pure white (pixel value of 255). This setting is increase by 1 for each unsuccessful iteration of the captcha breaker, in case the returned value does not match the length of`captcha_text_length` (see below).**The avg_deviation also dictates how many iterations the captcha breaker should attempt before giving up.**
   2) `u_filter`: short for scipy's "uniform filter", which compares each pixel to its direct neighbours and converts the pixel to the brightness of the majority of pixels that surround it. The u_filter value specifies how many pixels it should compare the current pixel with.
   3) `captcha_text_length`: the number of digits in the captcha.
2) Logger >__init__.py, line 6:`logger.setLevel(logging.WARN)`

   1) This sets the minimum log value that is printed onto the terminal when the code is run. To see all logs, change this to`logger.setLevel(logging.INFO)`.


**FURTHER DEVELOPMENT**

1. Instead of only`avg_deviation` being changed in each iteration, ideally it would cover every possible permutation of`avg_deviation` and`u_filter` until a solution is found.

1) This code rellies on Pytesseract to work. Ideally it would use its own trained model instead.



LICENSE

[Apache License, version 2.0]()
