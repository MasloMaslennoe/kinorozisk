from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def add_movie_review(request):
    if not request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        movie_id = request.POST.get('movie_id')
        MovieReview.objects.create(
            author = request.user,
            movie = Movie.objects.get(id = movie_id),
            text = request.POST.get('review_text'),
        )
        return redirect('movie_detail',movie_id=movie_id)

def persons_list(request, person_role):
    persons = MoviePerson.objects.filter(role = person_role).order_by('-id')
    if person_role == MoviePerson.RoleType.ACTOR:
        title = 'Актеры'
    else:
        title = 'Режиссеры'
    
    return render(request, 'kinorozisk/list/actors_list.html',{
        'persons': persons, 'title': title
    })

def genres_list(request):
    genres = Genre.objects.all()
    return render(request, 'kinorozisk/list/genres_list.html',{
        'genres': genres
    })

def movies_list(request):
    movies = Movie.objects.all()
    return render(request, 'kinorozisk/list/movies_list.html', {
        'movies': movies
    })

def person_detail(request, person_id):
    person = MoviePerson.objects.get(id=person_id)
    if person.role == MoviePerson.RoleType.ACTOR:
        movies = person.acted_in_movies.all()
        role_name = 'Актер'
    else:
        movies = person.directed_movies.all()
        role_name = 'Режиссер'
    return render(request, 'kinorozisk/detail/actor_detail.html',{
        'person': person,
        'movies': movies,
        'role_name': role_name
    })

def genre_detail(request, genre_id):
    genre = Genre.objects.get(id=genre_id)
    movies = genre.movies.all()
    return render(request, 'kinorozisk/detail/genre_detail.html',{
        'genre': genre
    })

def movie_detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'kinorozisk/detail/movie_detail.html',{
        'movie': movie,
        'reviews': MovieReview.objects.filter(movie_id=movie_id)
    })

def home (request):
    movies = Movie.objects.all()

    context = {
        'movies':movies
    }

    return render(request, 'kinorozisk/home.html', context)