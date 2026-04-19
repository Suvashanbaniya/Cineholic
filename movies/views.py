from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages 
from .models import Movie, Rating


# Create your views here.
def home(request):
    item = Movie.objects.first()
    
    return render(request,"home.html",{"item":item})


def rating(request,movie_id):
    if request.method =="POST":
        rating_value = request.POST.get("rating")
        review_text = request.POST.get("review")
        
        movie = Movie.objects.get(id=movie_id)
        
        Rating.objects.create(
            rating=rating_value,
            review=review_text,
            movie=movie
        )
        return HttpResponse("Rating is stored successfully")
    return HttpResponse("Send a POST request with rating and review data")
        
    
        
    
    
#browse page
def browse(request):
    return HttpResponse("Browse movies here !")

#movie detail page
def movie_detail(request,pk):
    return HttpResponse(f"Movie detail page for movie id {pk}");


#series_detail page 
def series_detail(request,pk):
    return HttpResponse(f"This is the series detail page for series id {pk}")

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

def login(request):
    return HttpResponse("Login page")

def register(request):
    return HttpResponse("Register page")