from django.contrib.auth.models import AbstractUser, PermissionsMixin, Group, Permission
from django.db import models
from django.contrib.auth.hashers import make_password, check_password


class Userdatamodel(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(max_length=50)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)  # Compare raw password with hashed password

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        super().set_password(raw_password)

    groups = models.ManyToManyField(Group, related_name='userdatamodel_set')
    user_permissions = models.ManyToManyField(Permission, related_name='userdatamodel_set')

    class Meta:
        db_table = 'userdata_table'

