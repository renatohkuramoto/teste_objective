from dataclasses import dataclass

from bank.models import Account


@dataclass
class TransactionData:
    valor: float
    forma_pagamento: str
    valor_fee: float
    valor_total: float
    conta: Account
