from django.core.exceptions import ObjectDoesNotExist
from typing import Dict, List

from bank.models import Account


class AccountRepository:
    @staticmethod
    def get_all() -> List[Account]:
        return Account.objects.all()

    @staticmethod
    def get_by_number(account_number: int) -> Account | None:
        try:
            return Account.objects.filter(conta_id=int(account_number)).get()
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def exists(account_number: int) -> bool:
        return Account.objects.filter(conta_id=int(account_number)).exists()

    @staticmethod
    def save(data: Dict):
        return Account.objects.create(**data)
