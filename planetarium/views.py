from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from planetarium.models import ShowTheme, AstronomyShow
from planetarium.serializers import ShowThemeSerializer, AstronomyShowSerializer


class ShowThemeViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = ShowTheme.objects.all()
    serializer_class = ShowThemeSerializer


class AstronomyShowViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = AstronomyShow.objects.all()
    serializer_class = AstronomyShowSerializer
