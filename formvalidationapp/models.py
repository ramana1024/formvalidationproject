from django.db import models

class registrationdata(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    email=models.EmailField(max_length=20)
    password1=models.CharField(max_length=20)
    password2=models.CharField(max_length=20)
    mobile=models.BigIntegerField()
