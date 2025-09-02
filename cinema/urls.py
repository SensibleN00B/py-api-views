from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import GenreListCreateAPIView, GenreDetailAPIView, ActorListCreateAPIView, ActorDetailAPIView, \
    CinemaHallViewSet, MovieViewSet

router = DefaultRouter()
router.register(r"cinema_halls", CinemaHallViewSet)
router.register(r"movies", MovieViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("genres/", GenreListCreateAPIView.as_view(), name="genre-list-create"),
    path("genres/<int:pk>/", GenreDetailAPIView.as_view(), name="genre-detail"),
    path("actors/", ActorListCreateAPIView.as_view(), name="actors-list-create"),
    path("actors/<int:pk>/", ActorDetailAPIView.as_view(), name="actor-detail"),
]

app_name = "cinema"
