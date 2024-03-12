from django.forms.models import model_to_dict
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from bank.helpers.data_classes import TransactionData
from bank.helpers.enums import TransactionFee
from bank.serializers import TransactionModelSerializer, TransactionSerializer
from bank.repository import AccountRepository, TransactionRepository


class TransactionView(APIView):
    def get(self, request):
        query_params = request.GET

        transaction_id = query_params.get("id")

        if transaction_id:
            transaction = TransactionRepository.get_by_id(transaction_id=transaction_id)
            if not transaction:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = TransactionModelSerializer(transaction)
            return Response(status=status.HTTP_200_OK, data=serializer.data)

    def post(self, request):
        serializer = TransactionSerializer(data=request.data)

        if serializer.is_valid():
            data = serializer.data

            account_number = data["conta_id"]
            payment_type = data["forma_pagamento"]
            value = data["valor"]
            fee = TransactionFee[payment_type].value

            account = AccountRepository.get_by_number(account_number)

            if not account:
                return Response(
                    status=status.HTTP_400_BAD_REQUEST,
                    data={"message": "Conta não encontrada"},
                )

            transaction_fee = (value / 100) * fee
            transaction_value = value + transaction_fee

            if account.valor == 0 or account.valor < transaction_value:
                return Response(
                    status=status.HTTP_400_BAD_REQUEST,
                    data={"message": "Saldo insulficiente para a operação"},
                )

            # Bloqueia o valor antes da transação
            TransactionRepository.block_balance(
                account=account, transaction_value=transaction_value
            )

            try:
                transaction = TransactionRepository.save(
                    transaction=TransactionData(
                        valor=value,
                        forma_pagamento=payment_type,
                        valor_fee=transaction_fee,
                        valor_total=transaction_value,
                        conta=account,
                    )
                )
            except Exception:
                # Chargeback pois houve algum erro
                TransactionRepository.chargeback(
                    account=account, transaction_value=transaction_value
                )
                return Response(status=status.HTTP_400_BAD_REQUEST)

            return Response(status=status.HTTP_200_OK, data=model_to_dict(transaction))
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
