from rest_framework import generics, pagination
from api.models import Movie
from api.serializers import MovieSerializer
from api.permissions import IsAdminOrReadOnly
class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = pagination.LimitOffsetPagination
