from domain.base import BaseModel
from django.db import models

from . import Category, Dictionary


class Word(BaseModel):
    dictionary = models.ForeignKey(Dictionary, on_delete=models.PROTECT, blank=False)
    title = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=False)
    category = models.ManyToManyField(Category)
