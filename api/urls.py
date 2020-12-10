from api.views import (
    MovieListCreateView,
    MovieDetailView,
    search_movies
)
from django.urls import include, path

urlpatterns = [
    path("movies/", MovieListCreateView.as_view(), name="movies"),
    path("movies/search/", search_movies, name="search_movie"),
    path("movies/<pk>/", MovieDetailView.as_view(), name="movie"),
]
