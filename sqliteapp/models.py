from django.db import models

class Customer(models.Model):
    id = models.CharField(primary_key=True,max_length=200)
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    address = models.CharField(max_length=300)

    def __str__(self):
        return self.name