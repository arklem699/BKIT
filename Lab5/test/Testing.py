from math import *
from main import *
import unittest
from behave import Given, Then, When

class Test_get_rootsTTD(unittest.TestCase):
    def test1(self):
        self.assertEqual(get_roots(1, -4, 4), [sqrt(2), -sqrt(2)])

    def test2(self):
        self.assertEqual(get_roots(9, -10, 1), [1, -1, 1/3, -1/3])

    def test3(self):
        self.assertEqual(get_roots(0, 1, -4), [-2, 2])

    def test4(self):
        self.assertEqual(get_roots(1, 11, 10), [])


@Given("Data for equation")
def test1():
    print("Data for equation")
    print(f"Data: {[9, -10, 1]}")
    print(f"Data: {[1, -4, 4]}")


@When("I want to solve the equation")
def test2():
    print("I want to solve the equation")


@Then("I get roots")
def test3():
    print("I get roots")
    assert get_roots(9, -10, 1) == [1, -1, 1/3, -1/3]
    assert get_roots(1, -4, 4) == [sqrt(2), -sqrt(2)]


def main():
    unittest.main()


if __name__ == '__main__':
    unittest.main()