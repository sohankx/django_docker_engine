import django

from .settings_common import *  # noqa
from .utils import hostname

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': False,
        'DIRS': [__package__]
    },
]

STATIC_URL = '/static/'

ALLOWED_HOSTS = ['*', 'localhost', '127.0.0.1', hostname()]
# hostname() allows the docker containers to
# get files from the upload directory on this server.

if django.VERSION >= (2, 0):
    MIDDLEWARE = shared_middleware  # noqa: F405
else:
    MIDDLEWARE_CLASSES = shared_middleware  # noqa: F405

# TODO: fix copy and paste between this and demo_path_routing_auth/settings.py
