from flask import jsonify
from flask.wrappers import Response
from typing import Union


def json_api_response(*args, **kwargs) -> Response:
    """Wrapper around jsonify that sets the Content-Type of the response
    to application/vnd.api+json.
    """

    response = jsonify(*args, **kwargs)
    response.mimetype = 'application/vnd.api+json'
    return response


def jsonapi_errors(errors: list):
    return {'errors': errors, 'jsonapi': {'version': '1.0'}}


def json_api_errors(errors: Union[list, Response]) -> Response:
    """Wrapper around json_api_response that returns a list of errors as
    a json-api like response.

    Args:
        errors: either an error Response or a list of dict error objects
    """

    # Already json api error
    if type(errors) == Response:
        return errors
    if type(errors) == list:
        return json_api_response(jsonapi_errors(errors))
    return json_api_response(errors)  # backup
