from django.db import models





class BcMember(models.Model):
    name = models.CharField(max_length=50, blank=True, null=False)
    gender = models.CharField(max_length=50, blank=True, null=False)
    age = models.IntegerField(max_length=50, blank=True, null=False)
    email = models.EmailField(max_length=50, blank=True, null=False)
    phone = models.CharField(max_length=50, blank=True, null=False)

def __str__(self):
    return self.name


class JrMember(models.Model):
    parent_name = models.CharField(max_length=50, blank=True, null=False)
    junior_name = models.CharField(max_length=50, blank=True, null=False)
    gender = models.CharField(max_length=50, blank=True, null=False)
    age = models.IntegerField(max_length=50, blank=True, null=False)
    parent_email = models.EmailField(max_length=50, blank=True, null=False)
    parent_phone = models.CharField(max_length=50, blank=True, null=False)


def __str__(self):
    return self.name


class AcMember(models.Model):
    name = models.CharField(max_length=50, blank=True, null=False)
    gender = models.CharField(max_length=50, blank=True, null=False)
    age = models.IntegerField(max_length=50, blank=True, null=False)
    email = models.EmailField(max_length=50, blank=True, null=False)
    phone = models.CharField(max_length=50, blank=True, null=False)


def __str__(self):
    return self.name

class Book(models.Model):
    Title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='uploads/images', null=False, blank=False, default="hjhjh")
    description = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.name