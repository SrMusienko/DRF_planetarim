from django.db.models import F, Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets
from rest_framework.viewsets import GenericViewSet

from planetarium.filters import AstronomyShowFilter
from planetarium.models import ShowTheme, AstronomyShow, PlanetariumDome, ShowSession
from planetarium.serializers import (
    ShowThemeSerializer,
    AstronomyShowSerializer,
    PlanetariumDomeSerializer,
    ShowSessionSerializer, AstronomyShowListSerializer, AstronomyShowDetailSerializer,
)


class ShowThemeViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = ShowTheme.objects.all()
    serializer_class = ShowThemeSerializer


class AstronomyShowViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = AstronomyShow.objects.all()
    serializer_class = AstronomyShowSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AstronomyShowFilter

    def get_serializer_class(self):
        if self.action == "list":
            return AstronomyShowListSerializer

        if self.action == "retrieve":
            return AstronomyShowDetailSerializer
        return AstronomyShowSerializer


class PlanetariumDomeViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = PlanetariumDome.objects.all()
    serializer_class = PlanetariumDomeSerializer


class ShowSessionViewSet(viewsets.ModelViewSet):
    queryset = (
        ShowSession.objects.all()
        .select_related("astronomy_show", "planetarium_dome")
        .annotate(
            tickets_available=(
                F("planetarium_dome__rows") * F("planetarium_dome__seats_in_row")
                - Count("tickets")
            )
        )
    )
    serializer_class = ShowSessionSerializer
