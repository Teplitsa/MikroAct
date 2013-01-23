# vim: fileencoding=utf-8 ai ts=4 sts=4 et sw=4
from django.db import models

from django.contrib.auth.models import User
from django.contrib.gis.db.models import PointField
from django.utils import timezone

from dj.choices import Choices
from dj.choices.fields import ChoiceField

from shortcuts import DefaultCharField, DEFAULT_CHARFIELD_LENGTH


class MikroAct(models.Model):
    title = DefaultCharField()
    date = models.DateField()
    description = models.TextField()
    author = models.ForeignKey(User)

    location_point = PointField(null=True)
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

    photo = models.ImageField(upload_to='mikro_act')

    objects = models.Manager()

    def __unicode__(self):
        return "%s (on %s)" % (self.name, self.date)


class CollectionMembership(models.Model):
    mikro_act = models.ForeignKey(MikroAct)
    collection = models.ForeignKey('Collection')
    date_joined = models.DateTimeField(default=timezone.now, editable=False)


class Collection(models.Model):
    name = DefaultCharField()
    author = models.ForeignKey(User)
    slug = models.SlugField(max_length=DEFAULT_CHARFIELD_LENGTH)

    is_private = models.BooleanField()
    date_created = models.DateTimeField(default=timezone.now, editable=False)

    mikro_acts = models.ManyToManyField(MikroAct, through=CollectionMembership)

    def __unicode__(self):
        return "%s (%d members)" % (self.name, self.mikro_acts.count())
