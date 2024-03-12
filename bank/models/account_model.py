from dataclasses import dataclass
from django.db import models


class Account(models.Model):
    id = models.AutoField(primary_key=True)
    conta_id = models.IntegerField()
    valor = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
