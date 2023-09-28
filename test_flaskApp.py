import unittest
import requests
from flask_app import app


class TestingFlask(unittest.TestCase):

    def test_hello_endpoint(self):
        response = requests.get("http://127.0.0.1:12121/hello")
        # response = app.test_client().get("/hello")
        # print(response)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "HELLO")


if __name__ == '__main__':
    unittest.main()
