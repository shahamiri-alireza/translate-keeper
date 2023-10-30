from uuid import uuid4 as GUID

from django.db import models


class Language(models.Model):
    id = models.UUIDField(default=GUID, editable=False, unique=True, primary_key=True)
    name = models.CharField(max_length=255)
    native_name = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=50)
    rtl = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.native_name} - {self.abbreviation}"
