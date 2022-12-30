from django.db import models
from django.utils import timezone


class Personal(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=20)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email


class Data(models.Model):
    person = models.ForeignKey(Personal, on_delete=models.CASCADE)
    height = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    comments = models.TextField()
    date = models.DateTimeField('date')

    def __str__(self):
        return self.person
