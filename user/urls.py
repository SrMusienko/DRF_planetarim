from user.views import CreateUserView, ManageUserView, CreateTokenView
from rest_framework_simplejwt import views as jwt_views
from django.http import JsonResponse
from django.urls import path
from django.urls import reverse


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
        "jws_token/",
        jwt_views.TokenObtainPairView.as_view(),
        name="jws_token_obtain_pair",
    ),
    path(
        "jws_token/refresh/",
        jwt_views.TokenRefreshView.as_view(),
        name="jws_token_refresh",
    ),
    path(
        "jws_token/verify/",
        jwt_views.TokenVerifyView.as_view(),
        name="jws_token_verify",
    ),
]
