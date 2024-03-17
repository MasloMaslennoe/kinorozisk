from django.shortcuts import render

# Create your views here.
def actors_list(request):
    return render(request, 'kinorozisk/list/actors_list.html')

def composers_list(request):
    return render(request, 'kinorozisk/list/composers_list.html')

def directors_list(request):
    return render(request, 'kinorozisk/list/directors_list.html')

def genres_list(request):
    return render(request, 'kinorozisk/list/genres_list.html')

def movies_list(request):
    return render(request, 'kinorozisk/list/movies_list.html')

def actor_detail(request, movie_id):
    return render(request, 'kinorozisk/detail/actor_detail.html')

def composer_detail(request, movie_id):
    return render(request, 'kinorozisk/detail/composer_detail.html')

def director_detail(request, movie_id):
    return render(request, 'kinorozisk/detail/director_detail.html')

def genre_detail(request, movie_id):
    return render(request, 'kinorozisk/detail/genre_detail.html')

def movie_detail(request, movie_id):
    return render(request, 'kinorozisk/detail/movie_detail.html')

def home (request):
    return render(request, 'kinorozisk/home.html')
