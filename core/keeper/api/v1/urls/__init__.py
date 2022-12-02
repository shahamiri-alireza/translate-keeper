from django.urls import path,include

urlpatterns = [
    path("category/", include('keeper.api.v1.urls.category'))
]