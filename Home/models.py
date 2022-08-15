from django.contrib.auth.models import User
from django.db import models


class CalorieModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    calorie = models.PositiveIntegerField()
    count = models.PositiveIntegerField(default=1)

    date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.user}:{self.name}:{self.calorie}'


class Hello(models.Model):
    name = models.CharField(max_length=10)
    num = models.PositiveIntegerField(default=1)
