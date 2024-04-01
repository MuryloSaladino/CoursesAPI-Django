from rest_framework.generics import CreateAPIView
from .models import Account
from .serializer import AccountSerializer


class AccountView(CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer