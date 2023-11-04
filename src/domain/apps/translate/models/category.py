from domain.base import BaseModel
from django.db import models

from .dictionary import Dictionary


class Category(BaseModel):
    title = models.CharField(max_length=255)
    color = models.CharField(max_length=25)
    dictionary = models.ForeignKey(Dictionary, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Categories"
