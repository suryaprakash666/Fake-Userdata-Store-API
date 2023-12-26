from django.db import models


# Create your models here.

class Userdatamodel(models.Model):
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)

    class Meta:
        db_table = 'api_userdatamodel'
