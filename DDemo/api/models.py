from django.db import models

# Create your models here.

class Module(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length = 12, null=True)


class Person(Module):
    age = models.CharField(max_length=50)