from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages 

# Create your views here.
def home(request):
    return HttpResponse("Welcome to cineholic! Explore movies, share reviews, and connect with fellow cinephiles. Your ultimate destination for all things cinema. Lights, camera, action!")

#browse page
def browse(request):
    return HttpResponse("Browse movies here !")

#movie detail page
def movie_detail(request,pk):
    return HttpResponse(f"Movie detail page for movie id {pk}");

#add content page
def add_content(request):
    return HttpResponse("Add content page")

#edit content page
def edit_content(request,pk):
    return HttpResponse(f"Edit content page for movie id {pk}")

#delete content page
def delete_content(request,pk):
    return HttpResponse(f"Delete content with id {pk}")

#delete review page
def delete_review(request,pk):
    return HttpResponse(f"Delete review with id {pk}")

#message function 
def message(request):
    messages.success(request,"Login successful")
    messages.error(request,"Error occurred")
    messages.warning(request,"This is Alarming")
    
    return HttpResponse("Message is written ")


#complain function
def complain(request):
    return HttpResponse(f"Complain what is wrong with the content ")