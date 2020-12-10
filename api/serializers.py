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
    """This is the serializer for displaying a Movie model"""
    genre = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = ["id", "name", "director", "genre", "imdb_score", "popularity"]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["genre"] = [genre.name for genre in instance.genre.all()]
        return data

    def to_internal_value(self, data):
        data = super().to_internal_value(data)
        data["genre"] = [{"name": genre} for genre in data["genre"]]
        return data

class MovieCreateSerializer(serializers.ModelSerializer):
    """
    This is the Serializer used for creating a Movie object.

    Since the genre field is a nested object, the `create` and `update` methods
    have been overridden.
    """
    genre = serializers.ListField(write_only=True, child=serializers.CharField())

    class Meta:
        model = Movie
        fields = ["id", "name", "director", "genre", "imdb_score", "popularity"]

    def create(self, validated_data):
        genre_data = validated_data.pop("genre")
        movie, _ = Movie.objects.get_or_create(**validated_data)
        for genre in genre_data:
            genre, _ = Genre.objects.get_or_create(name=genre)
            movie.genre.add(genre)
        return movie

    def update(self, instance, validated_data):
        genre_data = validated_data.pop("genre")
        Movie.objects.filter(pk=instance.id).update(**validated_data)

        for genre in genre_data:
            genre, _ = Genre.objects.get_or_create(name=genre)
            instance.genre.add(genre)
        return Movie.objects.get(pk=instance.id)

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
