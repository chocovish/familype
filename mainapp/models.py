from django.db import models
from django.contrib.auth.models import AbstractUser

class Family(models.Model):
    fam_name = models.CharField(max_length=30, default="My Family")
    balance = models.IntegerField(default=0)


class User(AbstractUser):
    usertype = models.CharField(max_length=5, choices=(('child','child'),('parent','parent')))
    phone = models.CharField(max_length=10)
    gender = models.CharField(max_length=1, choices=(('M','Male'),('F','Female'),('O','Other')))
    def name(self): return self.first_name +" "+ self.last_name
    family = models.ForeignKey(Family,on_delete=models.DO_NOTHING, blank=True, null=True)


class Transaction(models.Model):
    trans_id = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    amount = models.IntegerField()