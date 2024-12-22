from rest_framework.serializers import ModelSerializer

from apps.models import Film, Genre


class GenreModelSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']


class FilmModelSerializer(ModelSerializer):

    class Meta:
        model = Film
        fields = ['id', 'title']

    def to_representation(self, instance: Film):
        repr = super().to_representation(instance)
        repr['genres'] = [GenreModelSerializer(instance.genre.all()).data
        ]
        return repr


