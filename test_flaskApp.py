import unittest
from flask_app import app


class TestingFlask(unittest.TestCase):

    def test_hello_endpoint(self):
        response = app.test_client().get("/hello")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "HELLO")


if __name__ == '__main__':
    unittest.main()
