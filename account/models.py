from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Person(models.Model):
    MAN = 'XY'
    WOMAN='YY'
    SEX_CHOICE = [
        (MAN, 'Man'),
        (WOMAN, 'Woman')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    height = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    age = models.PositiveIntegerField(null=True)
    sex = models.CharField(max_length=10, choices=SEX_CHOICE, default='XY')
    bmr = models.PositiveIntegerField(null=True)

    # def bmr_computing(self,*args):
    #     if self.sex == 'XY':
    #         bmr = 66.47 + (13.75 * self.weight) + (5.003 * self.height) - (6.755 * self.age)
    #         self.bmr = bmr
    #         self.save()
    #     else:
    #         bmr = 655.1 + (9.563 * self.weight) + (1.850 * self.height) - (4.676 * self.age)
    #         self.bmr = bmr
    #         self.save()


