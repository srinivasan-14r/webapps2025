from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='register_userprofile')
    balance = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.user.username}'s profile"

class Transaction(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    receiver = models.CharField(max_length=255)  # or use ForeignKey if needed
    amount = models.FloatField()
    date_time = models.DateTimeField(auto_now_add=True)
