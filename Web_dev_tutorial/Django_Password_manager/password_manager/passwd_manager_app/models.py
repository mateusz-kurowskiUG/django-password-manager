from django.db import models
from django.contrib.auth.models import User

class PasswordSets(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="passwords",null=True)
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
class Accounts(models.Model):
    password_set = models.ForeignKey(PasswordSets,on_delete=models.CASCADE)
    acc_name = models.CharField(max_length=30)
    login = models.CharField(max_length=40)
    password = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name