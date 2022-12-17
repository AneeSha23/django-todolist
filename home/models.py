from django.db import models

# Create your models here.

class Todos(models.Model):
    list=models.CharField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)
