from django.contrib.auth import get_user_model

from domain.base import BaseModel
from django.db import models

from .language import Language

User = get_user_model()


class Dictionary(BaseModel):
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    name = models.CharField(max_length=255)
    language = models.ManyToManyField(Language)

    class Meta:
        verbose_name_plural = "Dictionaries"
