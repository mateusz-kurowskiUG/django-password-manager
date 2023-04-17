from django.db import models
from django.contrib.auth.models import User


class Accounts(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name="accounts")
    acc_name = models.CharField(max_length=30)
    login = models.CharField(max_length=40)
    password = models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.user},{self.acc_name},{self.login},{self.password}"
    
class User_avatar(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="passwd_manager_app/files/avatars",default="passwd_manager_app/files/avatars/mariusz_z_mieczem.jpg")
