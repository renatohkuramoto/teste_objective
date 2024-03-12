from django.core.exceptions import ObjectDoesNotExist

from bank.helpers.data_classes import TransactionData
from bank.models import Account, Transaction


class TransactionRepository:
    @staticmethod
    def get_by_id(transaction_id: int) -> Transaction | None:
        try:
            return Transaction.objects.filter(pk=int(transaction_id)).get()
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def save(transaction: TransactionData) -> Transaction:
        return Transaction.objects.create(
            valor=transaction.valor,
            forma_pagamento=transaction.forma_pagamento,
            valor_fee=transaction.valor_fee,
            valor_total=transaction.valor_total,
            conta_id=transaction.conta,
        )

    @staticmethod
    def block_balance(account: Account, transaction_value: float) -> None:
        account.valor -= transaction_value
        account.save()

    @staticmethod
    def chargeback(account: Account, transaction_value: float) -> None:
        account.valor += transaction_value
        account.save()
