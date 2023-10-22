import os
import time
from typing import Any

from werkzeug.exceptions import HTTPException

from flasgger import LazyJSONEncoder, LazyString
from flask import Flask, request, g
from cv_reader.utils import logging
from cv_reader.utils.rest import json_api_errors

env = os.environ.get('FLASK_ENV', 'dev')


def create_app(config_object: Any) -> Flask:
    app = Flask(__name__)

    from cv_reader.utils.converters import SectionConverter

    app.url_map.converters['section'] = SectionConverter

    # add flask configuration
    app.config.from_object(config_object)

    # ignore strict slashes; e.g. GET /test will be equivalent to GET /test/
    app.url_map.strict_slashes = False

    app.json_encoder = LazyJSONEncoder

    from cv_reader.routes import cv_blueprint
    from cv_reader.constants import exceptions
    app.register_blueprint(cv_blueprint)

    @app.errorhandler(exceptions.InvalidSectionException)
    def section_error_handler(e):
        return json_api_errors(
            [{
                'title': "Invalid Section",
                'detail': e.description,
            }]
        ), e.code

    return app
