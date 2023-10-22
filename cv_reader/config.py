class Config:
    APPLICATION_ROOT = '/'


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
