from sqliteapp.models import  Customer
from djongo import models

# Create your models here.
class Student(models.Model):
    tag = models.ArrayField()

    def __str__(self):
        return self.tag



