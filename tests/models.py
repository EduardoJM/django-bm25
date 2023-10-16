from django.db import models

class CharFieldModel(models.Model):
    app_label = 'app'
    field = models.CharField(max_length=64)
