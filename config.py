from logging import DEBUG
import os


class Config:
    '''
    General configuration parent class

    '''
    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.urandom(32)

    
class ProdConfig(Config):
    '''
    production configuration child class

    Args:
        config:  The parent configuration class with General configuration settings

    '''
    pass
class DevConfig(Config):
    '''
    Development configuration child class

    '''
    DEBUG = True


config_options = {
    'development':DevConfig,
    'production':ProdConfig
}
    