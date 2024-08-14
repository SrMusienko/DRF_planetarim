from django.http import JsonResponse
from django.urls import path, reverse
from rest_framework_simplejwt import views as jwt_views

from user.views import (
    CreateTokenView,
    CreateUserView,
    ManageUserView,
)


def api_root(request):
    return JsonResponse(
        {
            "register": request.build_absolute_uri(reverse("user:create")),
            "token": request.build_absolute_uri(reverse("user:token")),
            "me": request.build_absolute_uri(reverse("user:manage")),
            "jwt_token_obtain": request.build_absolute_uri(
                reverse("user:jwt_token_obtain_pair")
            ),
            "jwt_token_refresh": request.build_absolute_uri(
                reverse("user:jwt_token_refresh")
            ),
            "jwt_token_verify": request.build_absolute_uri(
                reverse("user:jwt_token_verify")
            ),
        }
    )


app_name = "user"


urlpatterns = [
    path("", api_root, name="api_root"),
    path("register/", CreateUserView.as_view(), name="create"),
    path("token/", CreateTokenView.as_view(), name="token"),
    path("me/", ManageUserView.as_view(), name="manage"),
    path(
        "jwt_token/",
        jwt_views.TokenObtainPairView.as_view(),
        name="jwt_token_obtain_pair",
    ),
    path(
        "jwt_token/refresh/",
        jwt_views.TokenRefreshView.as_view(),
        name="jwt_token_refresh",
    ),
    path(
        "jwt_token/verify/",
        jwt_views.TokenVerifyView.as_view(),
        name="jwt_token_verify",
    ),
]
