import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    HOST = os.environ.get('DB_HOST')
    PORT = os.environ.get('DB_PORT')
    DATABASE = os.environ.get('DB_DATABASE')
    USERNAME = os.environ.get('DB_USERNAME')
    PASSWORD = os.environ.get('DB_PASSWORD')
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    JWT_COOKIE_CSRF_PROTECT = False
    JWT_TOKEN_LOCATION = ["headers"]
    SECRET_KEY = os.environ.get('SECRET_KEY')
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')