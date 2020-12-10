from rest_framework import generics, pagination
from api.models import Movie
from api.serializers import MovieSerializer, MovieCreateSerializer
from api.permissions import IsAdminOrReadOnly
class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = pagination.LimitOffsetPagination

    def get_serializer_class(self):
        if self.request.method == "POST":
            return MovieCreateSerializer
        return MovieSerializer
