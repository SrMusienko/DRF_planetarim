import os
import tempfile

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from planetarium.models import (
    ShowTheme, AstronomyShow, PlanetariumDome, ShowSession,
)
from planetarium.serializers import ShowThemeSerializer, AstronomyShowListSerializer, AstronomyShowDetailSerializer

ASTRONOMY_SHOW_URL = reverse("planetarium:astronomy_show-list")
SHOW_SESSION_URL = reverse("planetarium:show_session-list")


def sample_astronomy_show(**params):
    defaults = {
        "title": "Sample show",
        "description": "Sample description",
    }
    defaults.update(params)

    return AstronomyShow.objects.create(**defaults)


def sample_show_theme(**params):
    defaults = {
        "name": "test",
    }
    defaults.update(params)

    return ShowTheme.objects.create(**defaults)


def sample_show_session(**params):
    planetarium_dome = PlanetariumDome.objects.create(
        name="Blue", rows=20, seats_in_row=20
    )

    defaults = {
        "show_time": "2022-06-02 14:00:00",
        "astronomy_show": None,
        "planetarium_dome": planetarium_dome,
    }
    defaults.update(params)

    return ShowSession.objects.create(**defaults)


def detail_url(astronomy_show_id):
    return reverse("planetarium:astronomy_show-detail", args=[astronomy_show_id])


class UnauthenticatedMovieApiTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        response = self.client.get(ASTRONOMY_SHOW_URL)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class AuthenticatedMovieApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email="test@test.test", password="testpassword"
        )
        self.client.force_authenticate(self.user)

    def test_astronomy_show_list(self):
        # Создание тестовых данных
        astronomy_show_with_theme = sample_astronomy_show()
        astronomy_show_with_theme.show_theme.add(sample_show_theme())

        # Выполнение запроса
        response = self.client.get(ASTRONOMY_SHOW_URL)

        # Получение данных из базы данных
        astronomy_shows = AstronomyShow.objects.all()
        serializer = AstronomyShowListSerializer(astronomy_shows, many=True)

        # Ожидаемые данные
        expected_data = {
            'count': astronomy_shows.count(),
            'next': None,
            'previous': None,
            'results': serializer.data
        }

        # Сравнение фактического и ожидаемого ответа
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)

    def test_filter_by_title(self):
        astronomy_show = sample_astronomy_show(title="Test")
        response = self.client.get(
            ASTRONOMY_SHOW_URL,
            {"title": astronomy_show.title}
        )

        astronomy_shows = AstronomyShow.objects.filter(title=astronomy_show.title)
        serializer = AstronomyShowListSerializer(astronomy_shows, many=True)

        expected_data = {
            'count': astronomy_shows.count(),
            'next': None,
            'previous': None,
            'results': serializer.data
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)

    def test_filter_by_actor_and_genre(self):
        astronomy_show = sample_astronomy_show(title="Test")
        theme = sample_show_theme(name="Art")
        astronomy_show.show_theme.add(theme)
        response = self.client.get(
            ASTRONOMY_SHOW_URL,
            {"show theme": f"{theme.id}"}
        )
        astronomy_shows = AstronomyShow.objects.filter(
            show_theme__id=theme.id,
        )
        serializer = AstronomyShowListSerializer(astronomy_shows, many=True)
        expected_data = {
            'count': astronomy_shows.count(),
            'next': None,
            'previous': None,
            'results': serializer.data
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)

    def test_retrieve_movie_detail(self):
        astronomy_show = sample_astronomy_show()
        astronomy_show.show_theme.add(ShowTheme.objects.create(name="Test theme"))
        url = detail_url(astronomy_show.id)
        response = self.client.get(url)
        serializer = AstronomyShowDetailSerializer(astronomy_show)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)


class AdminMovieTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email="admin@admin.test", password="testpassword", is_staff=True
        )
        self.client.force_authenticate(self.user)

    # def test_create_show_session_forbidden(self):
    #     payload = {
    #         "title": "Titanic",
    #         "duration": 195
    #     }
    #
    #     response = self.client.post(ASTRONOMY_SHOW_URL, payload)

    #    self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    def test_create_movie_with_genres_and_actors(self):
        theme_1 = ShowTheme.objects.create(name="Theme1")
        theme_2 = ShowTheme.objects.create(name="Theme2")

        payload = {
            "title": "Astronomy",
            "description": "The best astronomy show",
            "show_theme": [theme_1.id, theme_2.id],
        }
        response = self.client.post(ASTRONOMY_SHOW_URL, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_astronomy_show_not_allowed(self):
        astronomy_show = sample_astronomy_show()
        url = detail_url(astronomy_show.id)
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code,
            status.HTTP_405_METHOD_NOT_ALLOWED
        )
