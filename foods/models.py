from django.db import models


# Create your models here.

class Shop(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.name


class Food(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    shop = models.ManyToManyField(Shop)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
