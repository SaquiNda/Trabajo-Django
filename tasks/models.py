from pickle import TRUE
from pyexpat import model
from turtle import title
from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)