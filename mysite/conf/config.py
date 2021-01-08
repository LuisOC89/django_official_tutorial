# -*- coding: utf-8 -*-

import os
import configparser

# =============================================================================
# BASE APP CONFIGS
# =============================================================================
APP_NAME = 'mysite'
COMPANY = os.environ['COMPANY'] or 'lui'
APP_ENV = os.environ.get('APP_ENV') or 'local'  # or dev,stage,pilot,prod

# =============================================================================
# Load INI app config variables
# =============================================================================
INI_FILE = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    '{}-{}.ini'.format(COMPANY, APP_ENV))

CONFIG = configparser.ConfigParser()
CONFIG.read(INI_FILE)

# =============================================================================
# LOGGING Configuration
# =============================================================================
LOGGING_LEVEL = os.environ.get('LOGGING_LEVEL', CONFIG['LOGGING']['LEVEL'])

# =============================================================================
# DataBase Config
# =============================================================================
DB_HOST = os.environ['PJM_DB_SERVER']
DB_USER = os.environ['PJM_DB_USER']
DB_PWD = os.environ['PJM_DB_PWD']
DB_PORT = os.environ.get('PJM_DB_PORT', 5432)
DB_NAME = os.environ.get('PJM_DB_NAME', CONFIG['PGM_DB']['NAME'])

DATABASE_URL = f'postgresql+psycopg2://{DB_USER}:{DB_PWD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

DB_ECHO = False  # if CONFIG['database']['echo'] == 'yes' else False
DB_AUTOCOMMIT = True
CONNECT_TO_DATABASE = False

# =============================================================================
# Myloft Configuration
# =============================================================================
MYLOFT_KONG_URL = os.environ.get('MYLOFT_KONG_URL')
MYLOFT_HOST = os.environ.get('MYLOFT_HOST', CONFIG['MYCROFT']['HOST'])

# =============================================================================
# AWS Configuration
# =============================================================================
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']

# =============================================================================
# EZAPI Configuration
# =============================================================================
EZAPI_KONG_URL = os.environ.get('EZAPI_KONG_URL')
EZAPI_HOST = os.environ.get('EZAPI_HOST', CONFIG['EZAPI']['HOST'])

CONFIG_KEY = os.environ.get('CONFIG_KEY', '')

# =============================================================================
# REDIS Configuration
# =============================================================================
JWT_ALLOW_REFRESH = os.environ.get('JWT_ALLOW_REFRESH', CONFIG['JWT'].getboolean('ALLOW_REFRESH', fallback=False))

# =============================================================================
# REDIS Configuration
# =============================================================================
REDIS_HOST = os.environ['REDIS_HOST']
REDIS_PORT = os.environ.get('REDIS_PORT', 6379)
REDIS_EXPIRATION = os.environ.get('REDIS_EXPIRATION', 86400)  # 1 day
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD', "")
REDIS_KEY = "pjm"
REDIS_CACHE_DELETE_SIZE = int(os.getenv('REDIS_CACHE_DELETE_SIZE', '5000'))
REDIS_BATCH_SIZE = int(os.getenv('REDIS_BATCH_SIZE', '100'))

# =============================================================================
# Optional Fields
# =============================================================================
KONG_KEY = os.environ.get('KONG_KEY')

# =============================================================================
# Rest Client -> It has to go at the end so it
# recognizes all the variables declared in this module
# =============================================================================
# https://stackoverflow.com/questions/39402652/for-x-in-locals-runtimeerror-why-does-locals-change-size
# We need to declare a dummy variable so locals() doesn't change size
variable = ''
REST_CLIENT_DOMAINS = {}
for variable in globals():
    if variable.endswith(('_HOST', '_KONG_URL')):
        REST_CLIENT_DOMAINS[variable] = globals()[variable]
