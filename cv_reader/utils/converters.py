from werkzeug.routing import BaseConverter
from cv_reader.constants import exceptions


class SectionConverter(BaseConverter):

    def to_python(self, section):
        available_sections = ['personal', 'experience', 'education', 'skills']
        if section not in available_sections:
            raise exceptions.InvalidSectionException(
                f"The section you provided '{section}' is invalid, " +
                f'please choose one of: {available_sections}'
            )
        return section

    def to_url(self, section):
        return section
