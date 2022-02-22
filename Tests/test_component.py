#!python3

# Component test for captcha_solver. Checks that output matches the filename of the input file.

from os import path

import captcha_solver


class TestCaptchaSolverComponent:
    
    # TODO: test all images in Resources/in recursively
    def test_component(self):
        captcha_img_file = path.join("Tests", "Test_resources", "in", "2646.jpeg")
        expected_result = path.join(path.basename(captcha_img_file)).split('.')[0]
        out_img = path.join("Tests", "Test_resources", "out", path.basename(captcha_img_file))
        assert(captcha_solver.main(captcha_img_file, out_img)==expected_result)
