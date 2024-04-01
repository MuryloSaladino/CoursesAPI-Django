from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class Account(AbstractUser):
    
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    email = models.EmailField(unique=True, max_length=100)

    def __str__(self) -> str:
        return f"{self.id}"