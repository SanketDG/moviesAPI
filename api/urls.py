from api.views import (
    MovieListCreateView,
)
from django.urls import include, path

urlpatterns = [
    path("movies/", MovieListCreateView.as_view(), name="movies"),
]
