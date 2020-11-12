#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os


class Config(object):
    basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True


class DevelopmentConfig(Config):
    DEBUG = True
    # db
    DB_HOST = '00000'
    DB_PORT = 3306
    DB_USER = '000'
    DB_PASSWORD = '0000'
    DB_INSTANCE_NAME = 'aaaaaaaaaa'
    DB_CHARSET = 'utf8'


class ProductionConfig(Config):
    DEBUG = False
    # db
    DB_HOST = '00000'
    DB_PORT = 3306
    DB_USER = '000'
    DB_PASSWORD = '0000'
    DB_INSTANCE_NAME = 'aaaaaaaaaaaa'
    DB_CHARSET = 'utf8'


app_config = {
    'dev': DevelopmentConfig,
    'prod': ProductionConfig
}
