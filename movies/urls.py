from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('complain/',views.complain, name = 'complain'),
    path('browse/',views.browse, name='browse'),
    path('<int:pk>/',views.movie_detail, name='movie_detail'),
    path('add/',views.add_content, name='add_content'),
    path('<int:pk>/edit/',views.edit_content, name='edit_content'),
    path('<int:pk>/delete/',views.delete_content, name='delete_content'),
    path('review/<int:pk>/delete/',views.delete_review, name = 'delete_review'),
    path('message/',views.message, name ='message')
]