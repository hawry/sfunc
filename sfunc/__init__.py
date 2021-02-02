from .apigw_request import ApiGatewayRequest
from .apigw_response import ApiGatewayResponse


class SFunc(object):
    def __init__(self):
        self._handlers = {}
        self._default = None

    def _invalid_request_context(self, event, context):
        if self._default is not None:
            return self._default(event, context)
        raise ValueError('Invalid or missing requestContext')

    def _invalid_operation_name(self, event, context):
        if self._default is not None:
            return self._default(event, context)
        raise ValueError('Invalid or missing operationName in requestContext')

    def _sfunc_missing_operation_handler(self, req: ApiGatewayRequest, context):
        if self._default is not None:
            return self._default(req, context)
        raise ValueError(
            f"No operation with the name {req.operation_id} exists in {list(self._handlers.keys())}, and no default handler have been registered")

    def _missing_operation_handler(self, operation_name: str, event, context):
        if self._default is not None:
            return self._default(event, context)
        raise ValueError(
            f"No operation with the name {operation_name} exists in {list(self._handlers.keys())}, and no default handler have been registered")

    def sfunc_execute(self, req: ApiGatewayRequest, context) -> ApiGatewayResponse:
        handler = self._handlers.get(req.operation_id)
        if handler:
            return handler(req, context)
        return self._sfunc_missing_operation_handler(req, context)

    def execute(self, event, context):
        req_ctx = event.get('requestContext', None)
        if req_ctx is None or not isinstance(req_ctx, dict):
            return self._invalid_request_context(event, context)
        operation_name = req_ctx.get('operationName')

        if not operation_name:
            return self._invalid_operation_name(event, context)

        handler = self._handlers.get(operation_name)
        if handler:
            return handler(event, context)
        else:
            return self._missing_operation_handler(operation_name, event, context)

    def default(self):
        def decorator(f):
            self._default = f
            return f

        return decorator

    def operation(self, operation_name: str):
        def decorator(f):
            self._handlers[operation_name] = f
            return f

        return decorator
