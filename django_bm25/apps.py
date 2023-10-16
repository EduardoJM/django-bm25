from django.apps import AppConfig
from django.db.models import Field


class DjangoBm25Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_bm25'
