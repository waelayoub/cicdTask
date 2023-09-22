import unittest
import requests


class TestingFlask(unittest.TestCase):

    def test_hello_endpoint(self):
        response = requests.get("http://127.0.0.1:12121/hello")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "HELLO")


if __name__ == '__main__':
    unittest.main()
