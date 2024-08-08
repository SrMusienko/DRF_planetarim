import django_filters
from planetarium.models import AstronomyShow


class AstronomyShowFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr="icontains")
    description = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = AstronomyShow
        fields = ["title", "description"]
