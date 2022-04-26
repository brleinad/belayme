from django.db import models

from common.models import User


class MessengerBelayer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    messenger_id = models.BigIntegerField()
    photo = models.TextField()

    def __str__(self):
        return self.name

