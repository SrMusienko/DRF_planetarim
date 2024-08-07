from rest_framework import serializers

from planetarium.models import ShowTheme, AstronomyShow


class AstronomyShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = AstronomyShow
        fields = ("id", "title", "show_theme")


class ShowThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowTheme
        fields = ("id", "name", "astronomy_shows")
