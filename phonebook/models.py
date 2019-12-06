from django.db import models

from phonenumber_field.modelfields import *


class Phonebook(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)

    def __str__(self):
        return '%s %s' %(self.name, self.phone_number)

# Create your models here.
