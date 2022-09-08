from django.db import models


# Create your models here.
class InstaUser(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)

    def __str__(self):
        return self.username
