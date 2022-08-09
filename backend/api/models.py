from django.db import models


# Create your models here.
class User(models.Model):
    login = models.CharField(max_length=255, unique=True)
    user_id = models.IntegerField(unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.login
