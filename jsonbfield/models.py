from django.db import models
from jsonbfield.fields import JSONField

class JSONModel(models.Model):
    field = JSONField(blank=True, null=True)
