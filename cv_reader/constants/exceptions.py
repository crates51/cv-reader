from werkzeug.exceptions import HTTPException


class InvalidSectionException(HTTPException):
    code = 400
    description = "Invalid Section"
