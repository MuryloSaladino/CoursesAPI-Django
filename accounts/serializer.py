from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["id", "username", "password", "is_superuser", "email"]
        read_only_fields = ["id"]
        extra_kwargs = {
            "password": {"write_only": True},
            'username': {'validators': [
                UniqueValidator(
                    queryset=Account.objects.all(),
                    message="A user with that username already exists."
                )
            ]},
            'email': {'validators': [
                UniqueValidator(
                    queryset=Account.objects.all(),
                    message="user with this email already exists."
                )
            ]},
        }

    def create(self, validated_data):
        if validated_data.get("is_superuser"):
            account = Account.objects.create_superuser(**validated_data)
        else:
            account = Account.objects.create_user(**validated_data)
        return account