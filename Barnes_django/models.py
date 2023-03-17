from django.db import models



class User(models.Model):
    name = models.CharField(max_length=50, blank=True, null=False)
    gender = models.CharField(max_length=50, blank=True, null=False)
    age = models.IntegerField(max_length=50, blank=True, null=False)
    email = models.EmailField(max_length=50, blank=True, null=False)
    phone = models.CharField(max_length=50, blank=True, null=False)
    regID = models.CharField(max_length=50, blank=True, null=False)
    membership = models.CharField(max_length=50, blank=True, null=False)
    amount = models.IntegerField(max_length=50, blank=True, null=False)

def __str__(self):
    return self.name
