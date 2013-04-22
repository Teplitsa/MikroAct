# vim: fileencoding=utf-8 ai ts=4 sts=4 et sw=4
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from guardian.shortcuts import assign

@receiver(post_save, sender=User)
def set_default_permissions(sender, instance, created, **kwargs):
    if not created and not settings.DEBUG:
        return

    for perm in settings.DEFAULT_PERMISSIONS:
        p = assign(perm, instance)
