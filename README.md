# sfunc

[![PyPI version](https://badge.fury.io/py/sfunc.svg)](https://badge.fury.io/py/sfunc) [![hawry](https://circleci.com/gh/hawry/sfunc.svg?style=shield)](https://circleci.com/gh/hawry/sfunc) [![codecov](https://codecov.io/gh/hawry/sfunc/branch/master/graph/badge.svg?token=WPM7BHCN24)](https://codecov.io/gh/hawry/sfunc)

## Single lambda function for AWS Api Gateway

This is a very simple package which adds a few decorators to simplify the use of a single lambda function for multiple
endpoints for AWS Api Gateway. It uses the `operationId` attribute in the OAS3 specification to identify the correct
handler and then passes the event and context to the correct method.

### Basic usage

```python
import json
from sfunc import SFunc

sfunc = SFunc()


@sfunc.operation('getPetsByName')
def get_pets_by_name(event, context):
    """The methods need to have the same signature as a regular lambda handler entrypoint"""
    return {
        'statusCode': 200,
        'body': json.dumps({'names': ['fido', 'catty']})
    }


@sfunc.operation('getPetsByAge')
def get_pets_by_age(event, context):
    """This will be invoked when the endpoint with the operationId 'getPetsByAge' is invoked"""
    return {
        'statusCode': 204
    }


def lambda_handler(event, context):
    """We only need to specify one entry point and can ignore any other """
    rsp = sfunc.execute(event, context)  # rsp will contain the return value from the invoked method
    return rsp

```

### Using sfunc classes

For request/response which doesn't require any additional and are json encoded, sfunc provides two convenience classes
for request and response which can simplify the code further when it comes to parsing and getting headers and path
params. The following code will result in the same outcome as the example above, except for the extra headers.

```python
from sfunc import ApiGatewayRequest, ApiGatewayResponse, SFunc

sfunc = SFunc()


@sfunc.operation('getPetsByName')
def pets_by_name(req: ApiGatewayRequest, context) -> ApiGatewayResponse:
    _ = req.headers().get('x-request-id')
    return ApiGatewayResponse(200, {'names': ['fido', 'catty']})


@sfunc.operation('getPetsByAge')
def pets_by_age(req: ApiGatewayRequest, context) -> ApiGatewayResponse:
    rsp = ApiGatewayResponse(204)
    rsp.add_header('content-type', 'application/json')
    return rsp


def lambda_handler(event, context):
    return sfunc.sfunc_execute(ApiGatewayRequest(event), context).response()

```

### Specifying default handlers

It might be useful during development or if some endpoints are missing the operationId attribute in the specification.

```python

from sfunc import SFunc

sfunc = SFunc()


@sfunc.default()
def default_handler(event, context):
    return {
        'statusCode': 405
    }


def lambda_handler(event, context):
    return sfunc.execute(event, context)  # or sfunc.sfunc_execute(ApiGatewayRequest) -> ApiGatewayResponse as above

```
