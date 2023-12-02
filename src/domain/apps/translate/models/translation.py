from domain.base import BaseModel
from django.db import models

from . import Language, Word


class Translation(BaseModel):
    word = models.ForeignKey(Word, on_delete=models.PROTECT, blank=False, null=False)
    translate = models.CharField(max_length=255, blank=False, null=False)
    language = models.ForeignKey(
        Language, on_delete=models.PROTECT, blank=False, null=False
    )
