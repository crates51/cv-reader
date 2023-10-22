import os
import click

from flask.cli import FlaskGroup

from cv_reader import create_app
from cv_reader.config import configs
from cv_reader.routes.cv import fetch


env = os.environ.get('FLASK_ENV', 'dev')

# sets up the app
app = create_app(configs[env])
app.app_context().push()

cli = FlaskGroup(app)


def validate_section(ctx, param, section):
    available_sections = ['personal', 'experience', 'education', 'skills']
    if section not in available_sections:
        raise click.BadParameter(
            f"The value '{section}' you inserted is invalid; choose one of: {available_sections}"
        )
    return section


@cli.command()
@click.option('--section', prompt='Your section', callback=validate_section,
              help= "One of: ['personal', 'experience'. 'education', 'skills']")
def section(section):
    print(fetch(section)[0])


if __name__ == '__main__':
    cli()
