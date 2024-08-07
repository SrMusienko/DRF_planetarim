from django.urls import path, include
from rest_framework import routers

from planetarium.views import ShowThemeViewSet

# from cinema.views import (
#     GenreViewSet,
#     ActorViewSet,
#     CinemaHallViewSet,
#     MovieViewSet,
#     MovieSessionViewSet,
#     OrderViewSet,
# )
#
app_name = "planetarium"

router = routers.DefaultRouter()
router.register("show_theme", ShowThemeViewSet)
# router.register("actors", ActorViewSet)
# router.register("cinema_halls", CinemaHallViewSet)
# router.register("movies", MovieViewSet)
# router.register("movie_sessions", MovieSessionViewSet)
# router.register("orders", OrderViewSet)

urlpatterns = [path("", include(router.urls))]
