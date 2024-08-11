from django.urls import include, path
from rest_framework import routers

from planetarium.views import (
    AstronomyShowViewSet,
    PlanetariumDomeViewSet,
    ReservationViewSet,
    ShowSessionViewSet,
    ShowThemeViewSet,
)

app_name = "planetarium"

router = routers.DefaultRouter()
router.register(
    "show_themes",
    ShowThemeViewSet,
)
router.register("astronomy_shows", AstronomyShowViewSet, basename="astronomy_show")
router.register("planetarium_domes", PlanetariumDomeViewSet)
router.register("show_sessions", ShowSessionViewSet, basename="show_session")
router.register("reservations", ReservationViewSet)
urlpatterns = [path("", include(router.urls))]
