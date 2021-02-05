import json
import uuid


class ApiGatewayRequest:
    def __init__(self, event: dict):
        self._event = event
        self._json = None
        self._headers = None
        self._params = None
        self._stage_variables = None
        self._request_id = None
        self._operation_id = None
        self._set_metadata()

    def _set_metadata(self):
        if self._event is None:
            self._request_id = "m" + str(uuid.uuid4().hex)
            self._headers = {}
            self._params = {}
            self._json = {}
            self._stage_variables = {}
            return
        self._request_id = self._event.get('headers', {}).get('x-request-id', "m" + str(uuid.uuid4().hex))
        self._operation_id = self._event.get('requestContext', {}).get('operationName', None)
        self._authorizer = self._Authorizer(self._event.get('requestContext', {}))

    @property
    def operation_id(self):
        return self._operation_id

    @operation_id.setter
    def operation_id(self, value):
        self._operation_id = value

    @property
    def request_id(self) -> str:
        return self._request_id

    @request_id.setter
    def request_id(self, value: str):
        self._request_id = value

    def headers(self) -> dict:
        if self._headers is not None:
            return self._headers
        self._headers = self._event.get('headers', {})
        return self._headers

    def params(self) -> dict:
        if self._params is not None:
            return self._params
        self._params = self._event.get('pathParameters', {})
        return self._params

    def stage_variables(self) -> dict:
        if self._stage_variables is not None:
            return self._stage_variables
        self._stage_variables = self._event.get('stageVariables', {})
        return self._stage_variables

    def as_json(self) -> dict:
        if self._json is not None:
            return self._json

        if self._event is None or self._event.get('body', None) is None:
            self._json = {}
            return self._json

        try:
            self._json = json.loads(self._event.get('body'))
        except:
            self._json = {}
        return self._json

    def has_body(self) -> bool:
        return self.as_json() != {}

    def has_headers(self) -> bool:
        return self.headers() != {}

    def has_params(self) -> bool:
        return self.params() != {}

    def has_stage_variables(self) -> bool:
        return self.stage_variables() != {}

    @property
    def authorizer(self):
        return self._authorizer

    class _Authorizer:
        def __init__(self, request_context: {}):
            self._request_context = request_context
            self._principal_id = self._request_context.get('authorizer', {}).get('principalId', None)
            self._context = self._request_context.get('authorizer', {}).get('context', None)

        @property
        def principal_id(self):
            return self._principal_id

        @property
        def context(self):
            return self._context
