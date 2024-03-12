from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from bank.repository import AccountRepository
from bank.serializers import AccountSerializer


class AccountView(APIView):
    def get(self, request):
        query_params = request.GET

        account_id = query_params.get("id")

        if account_id:
            account = AccountRepository.get_by_number(account_number=account_id)
            if account:
                serializer = AccountSerializer(account)
                return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = AccountSerializer(data=request.data)

        if serializer.is_valid():
            data = serializer.data
            has_account = AccountRepository.exists(data["conta_id"])

            if not has_account:
                AccountRepository.save(data)
                return Response(status=status.HTTP_201_CREATED, data=data)
            return Response(
                status=status.HTTP_422_UNPROCESSABLE_ENTITY,
                data={"message": "Conta já cadastrada."},
            )
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
