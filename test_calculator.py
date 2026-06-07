"""calculator 모듈 테스트."""

import unittest

from calculator import add, multiply, subtract


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_multiply(self):
        self.assertEqual(multiply(4, 3), 12)
        self.assertEqual(multiply(0, 5), 0)

    # NOTE: subtract() 함수에 대한 테스트가 아직 없습니다.


if __name__ == "__main__":
    unittest.main()
