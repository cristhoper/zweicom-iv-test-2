import unittest
import app

import requests


class TestMethods(unittest.TestCase):

    def test_fibonacci_math(self):
        self.assertEqual(app.fibonacci(0), 0)
        self.assertEqual(app.fibonacci(1), 1)
        self.assertEqual(app.fibonacci(2), 1)
        self.assertEqual(app.fibonacci(3), 2)
        self.assertEqual(app.fibonacci(4), 3)
        self.assertEqual(app.fibonacci(5), 5)

    def test_fibonacci_api_correct(self):
        self.assertEqual(app.fibonacci_element('6'), '8')
        self.assertEqual(app.fibonacci_element(6), '8')

    def test_fibonacci_api_incorrect(self):
        self.assertEqual(app.fibonacci_element('a'), "Input Error")

    # TODO missing tests for html

if __name__ == '__main__':
    unittest.main()
