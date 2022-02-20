from os import path

import captcha_solver


class TestCaptchaSolverComponent:
    
    # TODO: test all images in Resources/in recursively
    def test_component(self):
        captcha_img_file = path.join("Tests", "Test_resources", "2646.jpeg")
        expected_result = path.join(path.basename(captcha_img_file)).split('.')[0]
        assert(captcha_solver.main(captcha_img_file)==expected_result)
