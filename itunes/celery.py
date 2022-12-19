import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'itunes.settings.base')
celery = Celery('itunes')
celery.config_from_object('settings.conf:settings')
