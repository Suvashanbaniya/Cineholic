from django.db import models
from django.shortcuts import render 
from django.http import HttpResponse
from django.contrib import messages
from django.utils import timezone

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    Director = models.CharField(max_length=100)
    genre =models.TextField()
    
    

# Create your models here.
