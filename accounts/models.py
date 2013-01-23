# vim: fileencoding=utf-8 ai ts=4 sts=4 et sw=4
from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db.models import PointField

from userena.models import UserenaBaseProfile

from shortcuts import DefaultCharField


class UserProfile(UserenaBaseProfile):
    user = models.OneToOneField(User,
                                unique=True)
    location_point = PointField(null=True)
    location_address = DefaultCharField(blank=True)


class CollectiveMembership(models.Model):
    collective = models.ForeignKey('Collective')
    user_profile = models.ForeignKey(UserProfile)


class Collective(models.Model):
    # TODO should be related to a contrib.auth.models.Group for permissions

    location_point = PointField()
    location_address = DefaultCharField()

    description = models.TextField()

    photo = models.ImageField(upload_to='collective')

    members = models.ManyToManyField(UserProfile, through=CollectiveMembership)
