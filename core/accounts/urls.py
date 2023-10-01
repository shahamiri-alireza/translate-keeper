from django.urls import path, include

app_name = "accounts"

urlpatterns = [
    path("users/", include("accounts.api.v1.urls")),
    path("", include("djoser.urls")),
]
