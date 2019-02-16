from django.db import models
from django.contrib.auth.models import AbstractUser

class Family(models.Model):
    fam_name = models.CharField(max_length=30, default="My Family")
    balance = models.IntegerField(default=0)
    def __str__(self): return self.fam_name +" | "+ str(self.balance)


class User(AbstractUser):
# other attributes like email/first_name/last_name/date_registered already exists as we are extending the AbstructUser
    usertype = models.CharField(max_length=6, choices=(('child','Child'),('parent','Parent')))
    phone = models.CharField(max_length=10)
    gender = models.CharField(max_length=1, choices=(('M','Male'),('F','Female'),('O','Other')))
    birthday = models.DateField()
    def name(self): return self.first_name +" "+ self.last_name
    family = models.ForeignKey(Family,on_delete=models.DO_NOTHING, blank=True, null=True)


class Transaction(models.Model):
    trans_id = models.CharField(max_length=20)
    trans_type = models.CharField(max_length=1, choices=(('A','Add'),('P','Pay')))
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    amount = models.IntegerField()
    method = models.CharField(max_length=5, choices=(('paytm','Paytm'),('gpay','Google Pay'),('phope','PhonePe'),('wapp','WhatsApp'),('fmpay','FamPay')))
#   Better option: make a seperate model which will contain method types (eg. paytm/phonepe) and refer them in here(Transaction.method)
#   rather than storing method in a charfield. as for every transaction it will take some bytes of space in db for storing repetative data.
    def family(self): return self.user.family