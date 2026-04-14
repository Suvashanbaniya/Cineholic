from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Welcome to cineholic! Explore movies, share reviews, and connect with fellow cinephiles. Your ultimate destination for all things cinema. Lights, camera, action!")