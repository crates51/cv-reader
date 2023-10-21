from flask import Blueprint
from cv_reader.crud import cv
from cv_reader.schemas import CVSchema

cv_blueprint = Blueprint('cv', __name__, url_prefix = '/cv')


@cv_blueprint.route('/<section:section>', methods = ['GET'])
def fetch(section: str):
    """ Fetch sections from cv.
    Args:
        section: The cv section you want to retrieve, one of: ['personal',
            'experience'. 'education', 'skills'].
    Returns:
        CV section as an dict.
    """
    cv_data = cv.get()
    final_response = CVSchema(only=[section]).dump(cv_data)
    return final_response, 200
