from django.urls import path, re_path
from .views import AccountView, TransactionView


urlpatterns = [
    re_path(
        route=r"^conta",
        view=AccountView.as_view(),
        name="account",
    ),
    path(route="transacao", view=TransactionView.as_view(), name="transaction"),
]
