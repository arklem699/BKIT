import unittest
from main import fibonacci


class TEST(unittest.TestCase):
    def test1(self):
        self.assertEqual(list(fibonacci(3)), [1, 1, 2])

    def test2(self):
        self.assertEqual(list(fibonacci(5)), [1, 1, 2, 3, 5])

    def test3(self):
        self.assertEqual(list(fibonacci(7)), [1, 1, 2, 3, 5, 8, 13])


if __name__ == "__main__":
    unittest.main()