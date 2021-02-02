import unittest
from sfunc import ApiGatewayResponse


class ApiGatewayResponseTest(unittest.TestCase):
    def test_add_headers(self):
        sut = ApiGatewayResponse(200, {})
        sut.add_header('header1', 'header1value')
        sut.add_header('header2', 'header2value')
        self.assertDictEqual({'header1': 'header1value', 'header2': 'header2value'}, sut.headers)

    def test_set_headers(self):
        sut = ApiGatewayResponse(200, {})
        exp = {'header1': 'header1value', 'header2': 'header2value'}
        sut.headers = exp
        self.assertDictEqual(exp, sut.headers)

    def test_response_codes(self):
        sut = ApiGatewayResponse(200, {})
        self.assertEqual(200, sut.response_code)
        sut.response_code = 201
        self.assertEqual(201, sut.response_code)

    def test_body_contains_status_code(self):
        sut = ApiGatewayResponse(200)
        self.assertIsNone(sut.body)
        self.assertIsNone(sut.headers)
        self.assertEqual({'statusCode': 200}, sut.response())

    def test_set_body_and_headers(self):
        sut = ApiGatewayResponse(200)
        sut.body = {'hello': 'world'}
        sut.headers = {'header1': 'header1value'}
        self.assertEqual({'hello': 'world'}, sut.body)
        self.assertEqual({'statusCode': 200, 'body': '{"hello": "world"}', 'headers': {'header1': 'header1value'}},
                         sut.response())
