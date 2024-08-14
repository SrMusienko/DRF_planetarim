import django_filters

from planetarium.models import AstronomyShow, ShowSession


class AstronomyShowFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr="icontains")
    description = django_filters.CharFilter(lookup_expr="icontains")
    theme = django_filters.CharFilter(
        field_name="show_theme__name", lookup_expr="icontains"
    )

    class Meta:
        model = AstronomyShow
        fields = ["title", "description", "theme"]


class ShowSessionFilter(django_filters.FilterSet):
    show_time_start = django_filters.DateTimeFilter(
        field_name="show_time", lookup_expr="gte"
    )
    show_time_end = django_filters.DateTimeFilter(
        field_name="show_time", lookup_expr="lte"
    )
    astronomy_show_title = django_filters.CharFilter(
        field_name="astronomy_show__title", lookup_expr="icontains"
    )

    class Meta:
        model = ShowSession
        fields = ["show_time_start", "show_time_end", "astronomy_show_title"]
