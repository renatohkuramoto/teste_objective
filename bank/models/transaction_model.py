from django.db import models

from .account_model import Account


TRANSACTION_TYPES = {"P": "Pix", "C": "CreditCard", "D": "DebitCard"}


class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    valor = models.FloatField()
    forma_pagamento = models.CharField(
        max_length=1, choices=TRANSACTION_TYPES, blank=False, null=False
    )
    valor_fee = models.FloatField()
    valor_total = models.FloatField()
    conta_id = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="conta"
    )
    created_at = models.DateTimeField(auto_now_add=True)
