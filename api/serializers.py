from rest_framework import serializers
from api.models import Genre, Movie


class GenreSerializer(serializers.ModelSerializer):
    """
    GenreSerializer serializes a Genre Model.
    """
    class Meta:
        model = Genre
        fields = ["name"]


class MovieSerializer(serializers.ModelSerializer):
    """
    MovieSerializer for serializing into a Movie model.

    The only obstacle is that the genre field serializer expects a dict-like
    structure, so for each genre, we need to account that there
    is a whole string value and not a dict.

    This is handled in to_representation where the dict is created for each
    serialization.
    """
    genre = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = ["name", "director", "genre", "imdb_score", "popularity"]

    def to_representation(self, instance):
        """
        This method is overridden because GenreSerializer serializes
        to json using the GenreSerializer which adds a dict for every
        genre. Since we can show a flat list here, we convert the genre
        dicts to a flat array.
        """
        data = super().to_representation(instance)
        data["genre"] = [genre.name for genre in instance.genre.all()]
        return data
