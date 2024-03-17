from django.urls import path
from kinorozisk.views import *

urlpatterns = [
    path('', home, name='home'),

    path('actor_detail/<int:movie_id>/', actor_detail, name='actor_detail'),
    path('composer_detail/<int:movie_id>/', composer_detail, name='composer_detail'),
    path('director_detail/<int:movie_id>/', movie_detail, name='movie_detail'),
    path('genre_detail/<int:movie_id>/', genre_detail, name='genre_detail'),
    path('movie_detail/<int:movie_id>/', movie_detail, name='movie_detail'),
    
    path('actors_list/', actors_list, name='actors_detail'),
    path('composers_list/', composers_list, name='composers_detail'),
    path('directors_list/', directors_list, name='directors_detail'),
    path('genres_list/', genres_list, name='genres_detail'),
    path('movies_list/', movies_list, name='movies_detail'),  
]