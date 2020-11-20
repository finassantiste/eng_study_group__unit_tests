import unittest
from fina.code_challenges.is_he_gonna_survive.is_he_gonna_survive import is_he_gonna_survive


class MyTestWolfCase(unittest.TestCase):
    def test_method_exists(self):
        bullets = 0
        dragons = 0
        self.assertFalse(is_he_gonna_survive(bullets=bullets, dragons=dragons))


if __name__ == '__main__':
    unittest.main()
