# vim: fileencoding=utf-8 ai ts=4 sts=4 et sw=4
from django.contrib.auth.models import User
from django.contrib.gis.db.models import PointField
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone

from stream import utils

from shortcuts import DefaultCharField, DEFAULT_CHARFIELD_LENGTH


class UserProfile(models.Model):
    user = models.OneToOneField(User,
                                unique=True)
    location_point = PointField(null=True)
    location_address = DefaultCharField(blank=True)

    def __unicode__(self):
        return "profile for %s" % self.user.username


class Collective(models.Model):
    # TODO should be related to a contrib.auth.models.Group for permissions
    name = DefaultCharField()
    slug = models.SlugField(max_length=DEFAULT_CHARFIELD_LENGTH)

    location_point = PointField(null=True, blank=True)
    location_address = DefaultCharField(blank=True)

    description = models.TextField()

    photo = models.ImageField(upload_to='collective', null=True, blank=True)

    members = models.ManyToManyField(User, related_name='collectives',
            null=True, blank=True)

    date_created = models.DateTimeField(default=timezone.now, editable=False)

    def __unicode__(self):
        return "%s (%d members)" % (self.name, self.members.count())

    def get_absolute_url(self):
        return reverse("collective_detail", kwargs={"slug": self.slug})


utils.register_actor(User)
utils.register_target(Collective)
