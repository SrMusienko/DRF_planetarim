"""
URL configuration for DRF_Planetarium project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.http import JsonResponse
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularSwaggerView,
    SpectacularRedocView,
    SpectacularAPIView,
)
from rest_framework.reverse import reverse


def api_root(request):
    return JsonResponse(
        {
            "admin": request.build_absolute_uri(reverse("admin:index")),
            "api/planetarium/": request.build_absolute_uri("/api/planetarium/"),
            "api/user/": request.build_absolute_uri(reverse("user:api_root")),
            "api/doc/swagger/": request.build_absolute_uri("api/doc/swagger/"),
            "api/doc/redoc/": request.build_absolute_uri("api/doc/redoc/"),
        }
    )


urlpatterns = [
    path("", api_root, name="api_root"),
    path("admin/", admin.site.urls),
    path("api/planetarium/", include("planetarium.urls", namespace="planetarium")),
    path("api/user/", include("user.urls", namespace="user")),
    path("__debug__/", include("debug_toolbar.urls")),
    path(
        "api/doc/",
        SpectacularAPIView.as_view(),
        name="schema",
    ),
    path(
        "api/doc/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/doc/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"
    ),
]
