from django.urls import path, include
from rest_framework import routers

from planetarium.views import ShowThemeViewSet, AstronomyShowViewSet

app_name = "planetarium"

router = routers.DefaultRouter()
router.register("show_theme", ShowThemeViewSet)
router.register("astronomy_show", AstronomyShowViewSet)


urlpatterns = [path("", include(router.urls))]
