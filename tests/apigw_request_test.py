import unittest

from sfunc import ApiGatewayRequest


class ApiGatewayRequestTest(unittest.TestCase):

    def setUp(self) -> None:
        self.sut = with_params()

    def test_empty_event(self):
        self.sut = ApiGatewayRequest(None)
        self.assertTrue(self.sut.request_id.startswith('m'))
        self.assertFalse(self.sut.has_body())
        self.assertFalse(self.sut.has_headers())
        self.assertFalse(self.sut.has_params())
        self.assertFalse(self.sut.has_stage_variables())

    def test_has_operation_id(self):
        self.assertEqual('convert', self.sut.operation_id)
        self.sut.operation_id = 'operationid'
        self.assertEqual('operationid', self.sut.operation_id)

    def test_has_headers(self):
        self.assertTrue(self.sut.has_headers())
        self.assertEqual('application/json', self.sut.headers().get('Content-Type'))

    def test_has_body(self):
        self.assertTrue(self.sut.has_body())
        self.assertEqual({'data': 'world'}, self.sut.as_json())

    def test_request_id(self):
        self.assertEqual('behave-tests', self.sut.request_id)
        self.sut.request_id = 'requestid'
        self.assertEqual('requestid', self.sut.request_id)

    def test_has_params(self):
        self.assertTrue(self.sut.has_params())
        self.assertEqual('hello/world', self.sut.params().get('proxy'))

    def test_has_stage_variables(self):
        self.assertTrue(self.sut.has_stage_variables())
        self.assertEqual('avalue', self.sut.stage_variables().get('aname'))

    def test_get_principal_id(self):
        self.assertEqual('1932646a-8cfb-457d-97f5-dda3aaa7e43b', self.sut.authorizer.principal_id)


def with_params():
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
             'requestContext': {'resourceId': 'g2c3lv', "authorizer": {
                 "principalId": "1932646a-8cfb-457d-97f5-dda3aaa7e43b",
                 "integrationLatency": 0
             }, 'resourcePath': '/convert', 'operationName': 'convert',
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
    return ApiGatewayRequest(event)
