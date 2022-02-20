from os import path

import captcha_solver


class TestCaptchaSolverComponent:
    
    def test_component(self):
        captcha_img_file = path.join("Resources", "in", "2646.jpeg")
        expected_result = path.join(path.basename(captcha_img_file)).split('.')[0] + '\n'
        assert(captcha_solver.main(captcha_img_file)==expected_result)
