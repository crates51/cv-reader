class Config:
    APPLICATION_ROOT = '/'
    SWAGGER = {
        'uiversion': 3,
        'title': 'CJ BACKEND API',
        'version': '1.0.0',
        'headers': [
        ],
        'specs': [
            {
                'endpoint': '/swagger',
                'route': '/swagger.json',  # TODO: use HTTP_X_SCRIPT_NAME when set up
                'rule_filter': lambda rule: True,
                'model_filter': lambda tag: True,
            }
        ],
        'termsOfService': False,
        'swagger_ui': True,
        'specs_route': '/apidocs/',
        "static_url_path": "/flasgger_static",
        'swagger_ui_bundle_js': '//unpkg.com/swagger-ui-dist@3/swagger-ui-bundle.js',
        'swagger_ui_standalone_preset_js': '//unpkg.com/swagger-ui-dist@3/swagger-ui-standalone-preset.js', # noqa
        'jquery_js': '//unpkg.com/jquery@2.2.4/dist/jquery.min.js',
        'swagger_ui_css': '//unpkg.com/swagger-ui-dist@3/swagger-ui.css',
    }


class DevConfig(Config):
    DEBUG = True


class ProdConfig(Config):
    DEBUG = False


configs = {
    'dev': DevConfig,
    'development': DevConfig,
    'prod': ProdConfig,
    'production': ProdConfig,
}
