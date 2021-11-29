from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
class Crypt(models.Model):
    cryptname =models.CharField(max_length=20)
    def __str__(self) -> str:
        return  self.cryptname

class Cryptamount(models.Model):
    User = models.ForeignKey(User,related_name='Cryptamount', on_delete=models.CASCADE )
    amount = models.IntegerField(default=0)
    cryptid =models.ForeignKey(Crypt,on_delete=models.CASCADE)