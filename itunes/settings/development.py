from .base import *
from minio import Minio
from typing import List, Tuple


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': 'ashkan',
        'PASSWORD': '1234',
        'NAME': 'ashkan',
        'PORT': '5432'
    }
}

DEBUG = True

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': '',
}

MINIO_ENDPOINT = '127.0.0.1:9001'
MINIO_ACCESS_KEY = '1NC6XT6PloVFBH9T'
MINIO_SECRET_KEY = 'ohYb1G7qdnrfxRAqwXZHFgEpkEIB1O1r'
MINIO_USE_HTTPS = False

MINIO_PRIVATE_BUCKETS = [
    # --- unused buckets, included in migrations, django-minio-backends requires them
    'private',
    'test-private',
    'django-backend-dev-public',
    'django-backend-dev-private',
    'test-public',
    'public',
    'itunes-public2',
    'itunes',
]
MINIO_PUBLIC_BUCKETS = [
    'itunes-public',
    'itunes-private',
    'itunes-salable',
]
MINIO_POLICY_HOOKS: List[Tuple[str, dict]] = [
]
min_client = Minio(endpoint=MINIO_ENDPOINT,
                   access_key=MINIO_ACCESS_KEY,
                   secret_key=MINIO_SECRET_KEY,
                   secure=False
                   )
