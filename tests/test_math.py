import unittest
from mathFunctions.addition import addition


class TestMath(unittest.TestCase):
    def setUp(self):
        pass

    def test_addition(self):
        sum_nums = addition(3, 1)
        self.assertEqual(4, sum_nums)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
