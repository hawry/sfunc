import unittest

from sfunc import SFunc, ApiGatewayRequest, ApiGatewayResponse


class SFuncTest(unittest.TestCase):

    def test_execute_missing_request_context(self):
        sut = SFunc()
        with self.assertRaises(ValueError):
            sut.execute({}, None)

    def test_execute_missing_operation_name(self):
        sut = SFunc()
        with self.assertRaises(ValueError):
            sut.execute({'requestContext': {}}, None)

    def test_execute_not_found_operation_name(self):
        sut = SFunc()
        with self.assertRaises(ValueError):
            sut.execute({'requestContext': {'operationName': 'notfound'}}, None)

    def test_returns_correct_handler(self):
        sut = SFunc()

        @sut.operation('convert')
        def example_operation(event, context):
            return 'results'

        self.assertEqual('results', sut.execute(request_data(), None))

    def test_returns_default_handler_missing_request_context(self):
        sut = SFunc()

        @sut.default()
        def default_handler(event, context):
            return 'default_handler'

        self.assertEqual('default_handler', sut.execute({}, None))

    def test_returns_default_handler_missing_operation_name(self):
        sut = SFunc()

        @sut.default()
        def default_handler(event, context):
            return 'default_handler'

        self.assertEqual('default_handler', sut.execute({'requestContext': {}}, None))

    def test_returns_default_handler_not_found_operation_name(self):
        sut = SFunc()

        @sut.default()
        def default_handler(event, context):
            return 'default_handler'

        self.assertEqual('default_handler', sut.execute({'requestContext': {'operationName': 'notfound'}}, None))

    def test_sfunc_execute_returns_apigateway_response(self):
        sut = SFunc()

        @sut.operation('convert')
        def convert_op(req, context):
            return ApiGatewayResponse(200)

        actual = sut.sfunc_execute(ApiGatewayRequest(request_data()), None)
        self.assertIsInstance(actual, ApiGatewayResponse)

    def test_sfunc_execute_missing_default_handler_raises_error(self):
        sut = SFunc()
        with self.assertRaises(ValueError):
            sut.sfunc_execute(ApiGatewayRequest(request_data()), None)

    def test_sfunc_execute_returns_default_handler(self):
        sut = SFunc()

        @sut.default()
        def default_handler(req, context):
            return ApiGatewayResponse(200)

        actual = sut.sfunc_execute(ApiGatewayRequest(request_data()), None)
        self.assertIsInstance(actual, ApiGatewayResponse)


def request_data():
    event = {'resource': '/convert', 'path': '/convert', 'httpMethod': 'POST',
             'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Content-Type': 'application/json',
                         'Host': 'pldtgit0ba.execute-api.eu-west-1.amazonaws.com',
                         'X-Amzn-Trace-Id': 'Root=1-600c730b-01dfae4e4940eb40558cd2e3',
                         'x-api-key': 'LqgWQDhRz98l83dHMhbbO1ZgCIUBbK4I9QqDnhT8', 'X-Forwarded-For': '83.248.97.171',
                         'X-Forwarded-Port': '443', 'X-Forwarded-Proto': 'https', 'x-request-id': 'behave-tests'},
             'multiValueHeaders': {'Accept': ['*/*'], 'Accept-Encoding': ['gzip, deflate'],
                                   'Content-Type': ['application/json'],
                                   'Host': ['pldtgit0ba.execute-api.eu-west-1.amazonaws.com'],
                                   'User-Agent': ['python-requests/2.25.1'],
                                   'X-Amzn-Trace-Id': ['Root=1-600c730b-01dfae4e4940eb40558cd2e3'],
                                   'x-api-key': ['LqgWQDhRz98l83dHMhbbO1ZgCIUBbK4I9QqDnhT8'],
                                   'X-Forwarded-For': ['83.248.97.171'], 'X-Forwarded-Port': ['443'],
                                   'X-Forwarded-Proto': ['https'], 'x-request-id': ['behave-tests']},
             'queryStringParameters': {
                 "name": "me",
                 "multivalueName": "me"
             }, 'multiValueQueryStringParameters': {
            "name": [
                "me"
            ],
            "multivalueName": [
                "you",
                "me"
            ]
        }, 'pathParameters': {
            "proxy": "hello/world"
        },
             'stageVariables': {
                 "aname": "avalue"
             },
             'requestContext': {'resourceId': 'g2c3lv', 'resourcePath': '/convert', 'operationName': 'convert',
                                'httpMethod': 'POST', 'extendedRequestId': 'Znbp4GnTDoEFYeg=',
                                'requestTime': '23/Jan/2021:19:03:39 +0000', 'path': '/live/convert',
                                'accountId': '951170985986', 'protocol': 'HTTP/1.1', 'stage': 'live',
                                'domainPrefix': 'pldtgit0ba', 'requestTimeEpoch': 1611428619988,
                                'requestId': '996f77aa-2db8-4f1b-8fea-ee6d397172d3',
                                'identity': {'cognitoIdentityPoolId': None, 'cognitoIdentityId': None,
                                             'apiKey': 'LqgWQDhRz98l83dHMhbbO1ZgCIUBbK4I9QqDnhT8',
                                             'principalOrgId': None, 'cognitoAuthenticationType': None, 'userArn': None,
                                             'apiKeyId': 'zvxuavcnt4', 'userAgent': 'python-requests/2.25.1',
                                             'accountId': None, 'caller': None, 'sourceIp': '83.248.97.171',
                                             'accessKey': None, 'cognitoAuthenticationProvider': None, 'user': None},
                                'domainName': 'pldtgit0ba.execute-api.eu-west-1.amazonaws.com', 'apiId': 'pldtgit0ba'},
             'body': '{"data": "world"}', 'isBase64Encoded': False}
    return event
