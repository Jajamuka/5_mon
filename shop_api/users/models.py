from django.contrib.auth.models import User
from django.db import models


class ConfirmationCode(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)

    def __str__(self):
        return f"{self.user.username}: {self.code}"