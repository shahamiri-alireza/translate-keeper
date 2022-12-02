from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False)
    color = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
