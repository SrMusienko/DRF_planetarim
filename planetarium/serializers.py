from rest_framework import serializers

from planetarium.models import ShowTheme, AstronomyShow, PlanetariumDome, ShowSession


class ShowThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowTheme
        fields = ("id", "name", "astronomy_shows")


class AstronomyShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = AstronomyShow
        fields = ("id", "title", "description", "show_theme")


class AstronomyShowListSerializer(serializers.ModelSerializer):

    show_theme = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="name"
    )

    class Meta:
        model = AstronomyShow
        fields = (
            "id",
            "title",
            "description",
            "show_theme"
        )


class AstronomyShowDetailSerializer(serializers.ModelSerializer):
    show_theme = ShowThemeSerializer(many=True, read_only=True)

    class Meta:
        model = AstronomyShow
        fields = (
            "id",
            "title",
            "description",
            "show_theme"
        )


class PlanetariumDomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanetariumDome
        fields = ("id", "name", "rows", "seats_in_row")


class ShowSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowSession
        fields = ("id", "show_time", "astronomy_show", "planetarium_dome")
