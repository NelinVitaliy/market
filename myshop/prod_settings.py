import os
import json


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(BASE_DIR + '/config.json', 'r') as config:
    obj = json.load(config)


SECRET_KEY = obj["API_KEY"]

DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "161.35.158.21", "vitaemarket.kg"]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'market',
        'USER': 'userdb',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# STATIC_URL = '/shop/static/assets/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static/assets')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "shop/static", 'static')

