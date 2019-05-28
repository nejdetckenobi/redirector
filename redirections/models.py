from django.db import models


class Redirection(models.Model):
    unique_id = models.CharField(unique=True, max_length=128)
    url = models.CharField(max_length=256)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
