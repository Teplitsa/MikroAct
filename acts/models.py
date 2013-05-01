# vim: fileencoding=utf-8 ai ts=4 sts=4 et sw=4
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone

from follow import utils as follow_utils
from follow.models import Follow
from stream import utils as stream_utils
from geopy import geocoders

from shortcuts import DefaultCharField, DefaultDecimalField, DEFAULT_CHARFIELD_LENGTH


class MikroAct(models.Model):
    title = DefaultCharField()
    slug = models.SlugField(max_length=DEFAULT_CHARFIELD_LENGTH, unique=True)
    date = models.DateField()
    description = models.TextField()
    process = models.TextField(blank=True)
    author = models.ForeignKey(User, related_name='mikroacts')
    
    location_lat = DefaultDecimalField(editable=False, blank=True, null=True)
    location_lon = DefaultDecimalField(editable=False, blank=True, null=True)
    location_address = DefaultCharField(blank=True)

    date_created = models.DateTimeField(default=timezone.now, editable=False)
    is_published = models.BooleanField(default=True)

    photo = models.ImageField(upload_to='mikro_act', null=True, blank=True)

    objects = models.Manager()

    def __unicode__(self):
        return "%s (on %s)" % (self.title, self.date)

    def get_absolute_url(self):
        return reverse("mikroact_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        """ Set location from self.location_address, if possible

        FIXME: use different geocoder service
        FIXME: handle geocoding errors gracefully
        TODO: break out to separate function to expose as API view """
        if self.location_address:
            self.location_lat, self.location_lon = geocoders.GoogleV3().geocode(self.location_address)[1]
        super(MikroAct, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "MikroAct"


class Campaign(models.Model):
    name = DefaultCharField()
    author = models.ForeignKey(User)
    slug = models.SlugField(max_length=DEFAULT_CHARFIELD_LENGTH, unique=True)
    description = models.TextField(blank=True)
    is_private = models.BooleanField()
    date_created = models.DateTimeField(default=timezone.now, editable=False)

    mikro_acts = models.ManyToManyField(MikroAct, related_name='campaigns')

    def __unicode__(self):
        return "%s (%d mikroacts)" % (self.name, self.mikro_acts.count())

    def get_absolute_url(self):
        return reverse("campaign_detail", kwargs={"slug": self.slug})

    def is_followed_by(self, user):
        if not isinstance(user, User):
            raise TypeError(
                "Expecting django.contrib.auth.models.User, given %s" % type(user)
            )

        return Follow.objects.is_following(user, self)


stream_utils.register_target(MikroAct)
stream_utils.register_target(Campaign)
stream_utils.register_action_object(Campaign)  # for adding mikro acts

follow_utils.register(Campaign)
