from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return self.title
