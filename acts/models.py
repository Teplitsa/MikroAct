# vim: fileencoding=utf-8 ai ts=4 sts=4 et sw=4
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.gis.db.models import PointField
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone

from dj.choices import Choices
from dj.choices.fields import ChoiceField
from geopy import geocoders

from shortcuts import DefaultCharField, DEFAULT_CHARFIELD_LENGTH


class MikroAct(models.Model):
    title = DefaultCharField()
    slug = models.SlugField(max_length=DEFAULT_CHARFIELD_LENGTH, unique=True)
    date = models.DateField()
    description = models.TextField()
    author = models.ForeignKey(User)

    location_point = PointField(blank=True, null=True, editable=False)
    location_address = DefaultCharField(blank=True)

    class Statuses(Choices):
        _ = Choices.Choice
        call_to_action = _('Call to Action')
        in_progress = _('In Progress')
        complete = _('Complete')
    status = ChoiceField(choices=Statuses,
                         default=Statuses.call_to_action)

    date_created = models.DateTimeField(default=timezone.now, editable=False)
    is_published = models.BooleanField()

    photo = models.ImageField(upload_to='mikro_act', null=True, blank=True)

    objects = models.Manager()

    def __unicode__(self):
        return "%s (on %s)" % (self.title, self.date)

    def get_absolute_url(self):
        return reverse("mikroact_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        """ Set location_point from self.location_address, if possible

        FIXME: use different geocoder service
        FIXME: handle geocoding errors gracefully
        TODO: break out to separate function to expose as API view """
        if self.location_address:
            lat, lon = geocoders.Google().geocode(self.location_address)[1]
            print lat, lon
            self.location_point = "POINT(%s %s)" % (lon, lat)

        super(MikroAct, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "MikroAct"


class CollectionMembership(models.Model):
    mikro_act = models.ForeignKey(MikroAct)
    collection = models.ForeignKey('Collection')
    date_joined = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        unique_together = ('mikro_act', 'collection')


class CollectionFollow(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    collection = models.ForeignKey('Collection')
    date_followed = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        unique_together = ('user', 'collection')


class Collection(models.Model):
    name = DefaultCharField()
    author = models.ForeignKey(User)
    slug = models.SlugField(max_length=DEFAULT_CHARFIELD_LENGTH, unique=True)

    is_private = models.BooleanField()
    date_created = models.DateTimeField(default=timezone.now, editable=False)

    mikro_acts = models.ManyToManyField(MikroAct, through=CollectionMembership, related_name="collections")

    followers = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                       related_name='following',
                                       through=CollectionFollow)

    def __unicode__(self):
        return "%s (%d mikroacts)" % (self.name, self.mikro_acts.count())

    def get_absolute_url(self):
        return reverse("collection_detail", kwargs={"slug": self.slug})
