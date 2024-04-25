from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


