
from django.db import models

class User(models.Model):
    fname = models.CharField(max_length=100,unique=True)
    lname = models.CharField(max_length=100,unique=True)
    emails = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.fname