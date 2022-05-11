from app.tests import MyTestCase, test_client


class HomeTestCase(MyTestCase):

    def test_get_index(self):
        response = test_client.get("/")
        self.print.debug(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), { "message": "Hello World" })

    def test_get_info(self):
        response = test_client.get("/info")
        self.print.debug(response.text)
        self.assertEqual(response.status_code, 200)

    def test_http_exception_404(self):
        response = test_client.get("/exception/404")
        self.print.debug(response.text)
        self.assertEqual(response.status_code, 404)

    def test_custom_exception(self):
        response = test_client.get("/exception/custom")
        self.print.debug(response.text)
        self.assertEqual(response.status_code, 418)

    def test_exception_verify_token_and_key_NoHeader(self):
        response = test_client.get("/exception/secret")
        self.print.debug(response.text)
        self.assertEqual(response.status_code, 422)  # Validation Error

    def test_exception_verify_token_and_key_WithHeader(self):
        response = test_client.get("/exception/secret", headers = { "X-Token": "1", "X-Key": "2" })
        self.print.debug(response.text)
        self.assertEqual(response.status_code, 400)
