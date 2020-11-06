from .base import *
import os

DEBUG = True
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DEFUALT_NAME', 'knowledgebase'),
        'USER': os.environ.get('DEFAULT_USER', 'anal4'),
        'PASSWORD': os.environ.get('DEFAULT_PASSWORD', 'anal123'),
        'HOST': os.environ.get('DEFAULT_HOST', '192.168.1.21'),
        'PORT': os.environ.get('DFAULT_PORT', '3306'),
    }
}
