import json


class ApiGatewayResponse:
    def __init__(self, response_code: int, response_body=None):
        self._body = response_body
        self._headers = None
        self._response_code = response_code

    @property
    def headers(self) -> dict:
        return self._headers

    @headers.setter
    def headers(self, value: dict):
        self._headers = value

    def add_header(self, key: str, value: str):
        if self._headers is None:
            self._headers = {
                key: value
            }
        else:
            self._headers[key] = value

    @property
    def body(self) -> dict:
        return self._body

    @body.setter
    def body(self, value: dict):
        self._body = value

    @property
    def response_code(self) -> int:
        return self._response_code

    @response_code.setter
    def response_code(self, value: int):
        self._response_code = value

    def response(self) -> dict:
        rsp = {
            "statusCode": self._response_code or 200
        }
        if self._body is not None:
            rsp["body"] = json.dumps(self._body)
        if self._headers is not None:
            rsp['headers'] = self._headers
        return rsp
