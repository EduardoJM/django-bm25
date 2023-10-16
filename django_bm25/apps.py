from django.apps import AppConfig
from django.db.models import Field
from django_bm25.lookups import FullTextSearchLookup


class DjangoBm25Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_bm25'
