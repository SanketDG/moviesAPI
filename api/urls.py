from api.views import (
    MovieListCreateView,
    MovieDetailView
)
from django.urls import include, path

urlpatterns = [
    path("movies/", MovieListCreateView.as_view(), name="movies"),
    path("movies/<pk>/", MovieDetailView.as_view(), name="movie"),
]
