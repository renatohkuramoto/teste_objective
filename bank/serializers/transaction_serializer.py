from rest_framework import serializers

from bank.models import Transaction, TRANSACTION_TYPES
from bank.serializers.account_serializer import AccountSerializer


class TransactionSerializer(serializers.Serializer):
    forma_pagamento = serializers.ChoiceField(required=True, choices=TRANSACTION_TYPES)
    conta_id = serializers.IntegerField(required=True)
    valor = serializers.FloatField(required=True)


class TransactionModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = "__all__"
