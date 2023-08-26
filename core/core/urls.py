"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.urls import path, include
from configs.swagger import swagger_urlpatterns

apps_urlpatterns = [
    path("keeper/", include("keeper.api.v1.urls")),
    path("account/", include("dj_rest_auth.urls")),
    path("account/register/", include("dj_rest_auth.registration.urls")),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/v1/', include(apps_urlpatterns))
]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
        path("", include(swagger_urlpatterns)),
    ]
