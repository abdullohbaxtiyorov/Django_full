from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView

from apps.models import Film, Genre
from apps.serializers import FilmModelSerializer, GenreModelSerializer


@extend_schema(tags=['Films'])
class FilmListCreateAPIView(ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmModelSerializer


@extend_schema(tags=['Genres'])
class GenreListCreateAPIView(ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreModelSerializer
