from django.core.management.base import BaseCommand, CommandError
from api.models import Movie, Genre
from django.conf import settings
import json


class Command(BaseCommand):
    help = 'Imports JSON file given as argument into the database'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str)

    def handle(self, *args, **kwargs):

        if kwargs.get("json_file") is None:
            self.stdout.write(self.style.ERROR(f"No file has been supplied."))
        else:
            json_file = kwargs.get("json_file")
            with open(json_file) as file:
                for movie in json.loads(file.read()):
                    genre_dict = movie.pop("genre")
                    movie["popularity"] = movie["99popularity"]
                    movie.pop("99popularity")
                    movie_obj, _ = Movie.objects.get_or_create(**movie)
                    movie_obj.save()

                    for genre in genre_dict:
                        genre_obj, _ = Genre.objects.get_or_create(name=genre.strip())
                        movie_obj.genre.add(genre_obj)

            self.stdout.write(self.style.SUCCESS('JSON File imported'))
            return None

