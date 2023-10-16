from django.db import models
from django.db.models import Q
from django.db.models import manager
from django.db.models.expressions import Expression
from django_bm25.indexes import Bm25Index
from django_bm25.mixins import FullTextSearchMixin
from django.db.models.sql.where import ExtraWhere, AND

class Star(Expression):
    def __repr__(self):
        return "'*'"

    def as_sql(self, compiler, connection):
        db_table = compiler.query.get_meta().db_table
        return "%s.*" % db_table, []

class City(FullTextSearchMixin, models.Model):
    code = models.CharField("Code", max_length=7, unique=True)
    name = models.CharField("Name", max_length=255)
    state = models.CharField("State", max_length=2)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
        indexes = [
            Bm25Index(
                Star(),
                name='idx_city_name',
                text_fields={
                    'name': {
                        'tokenizer': 'whitespace',
                        'normalizer': 'lowercase'
                    }
                }
            ),
        ]

