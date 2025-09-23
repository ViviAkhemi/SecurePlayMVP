'''
teste:
from django.db import models

class Progress(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
'''
from django.db import models
from django.contrib.auth.models import User

class UserProgress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    badges = models.JSONField(default=list)  # lista de medalhas

    def __str__(self):
        return f"{self.user.username} - {self.points} pts"
