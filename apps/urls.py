from django.urls import path

from apps.views import FilmListCreateAPIView, GenreListCreateAPIView

urlpatterns = [
    path('film/', FilmListCreateAPIView.as_view()),
    path('genre/', GenreListCreateAPIView.as_view()),
]
