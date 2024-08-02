import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'mysql://avnadmin:AVNS_iNf7uPwTKi16T5Adrcj@mysql-1206eb68-hyperlocaloffers.e.aivencloud.com:24725/defaultdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
