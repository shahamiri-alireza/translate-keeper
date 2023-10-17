from django.db import models
from django.utils.translation import gettext_lazy as _

from domain.base import BaseModel

class LoginAttempt(BaseModel):
    username = models.CharField(_("username"), max_length=255, blank=True, null=True)
    password = models.CharField(_("password"), max_length=255, blank=True, null=True)
    ip = models.GenericIPAddressField(_("ip address"), protocol='both', blank=True, null=True)
    session_key = models.CharField(_("session key"), max_length=50, blank=True, null=True)
    user_agent = models.TextField(_("user-agent"), blank=True, null=True)
    path = models.TextField(_("path"), blank=True, null=True)

    class Meta:
        verbose_name = _("Honeypot Login Attempt")
        verbose_name_plural = _("Honeypot Login Attempts")
        ordering = ('-created_date',)

    def __str__(self):
        return self.username