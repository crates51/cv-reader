import logging


def get_logger():
    logger = logging.getLogger('cj-backend')
    logger.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        '[%(levelname)s] [%(asctime)s] '
        'method=%(method)s | '
        'endpoint=%(endpoint)s | '
        'query_params=%(query_params)s | '
        'request_duration=%(request_duration)s | '
        'status_code=%(status_code)s  | '
        'body=%(body)s | '
        'response=%(message)s '
        'error=%(error)s '
        # noqa: E502
    )
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger


def get_logger_data(request, response, request_duration, error = None):
    return {
        'method': request.method,
        'endpoint': request.path,
        'query_params': request.query_string.decode(),
        'request_duration': request_duration,
        'status_code': response.status_code,
        'body': request.get_data().decode(),
        'error': error
    }
