from django.urls import path,include

urlpatterns = [
    path("category/", include('keeper.api.v1.urls.category')),
    path("word/", include('keeper.api.v1.urls.word'))
]