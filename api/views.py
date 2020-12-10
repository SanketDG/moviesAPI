from django.db.models import Q
from rest_framework import generics, pagination, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

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

@api_view(["GET"])
def search_movies(request):
    """
    Search movies by query on name, director or genre
    """
    search_query = request.GET.get("q", None)
    print(search_query)
    if search_query is not None:
        print(search_query)
        search_results = Movie.objects.filter(
            Q(name__icontains=search_query)
            | Q(director__icontains=search_query)
            | Q(genre__name__icontains=search_query)
        )

        search_serialized = MovieSerializer(search_results, many=True)
        return Response(search_serialized.data, status=status.HTTP_200_OK)
    return Response({"message": "Search query missing"}, status=status.HTTP_200_OK)
