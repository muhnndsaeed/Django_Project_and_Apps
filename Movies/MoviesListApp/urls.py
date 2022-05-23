from django.urls import path
import MoviesListApp.views

urlpatterns = [path('', MoviesListApp.viwes.Movie_name,name='Movie_Name')]