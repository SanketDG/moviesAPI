from rest_framework import generics, pagination
from api.models import Movie
from api.serializers import MovieSerializer, MovieCreateSerializer
from api.permissions import IsAdminOrReadOnly
class MovieListCreateView(generics.ListCreateAPIView):
    """
    This is the view that is responsible for listing and creating movies

    """
    queryset = Movie.objects.all()
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = pagination.LimitOffsetPagination

    def get_serializer_class(self):
        if self.request.method == "POST":
            return MovieCreateSerializer
        return MovieSerializer

class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Responsible for updating, deleting and retrieving movie details
    """
    permission_classes = [IsAdminOrReadOnly]
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == "PUT" or self.request.method == "PATCH":
            return MovieCreateSerializer
        return MovieSerializer
