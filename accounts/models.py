# vim: fileencoding=utf-8 ai ts=4 sts=4 et sw=4 from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.comments.models import Comment
from django.db import models
from django.utils import timezone

from follow import utils as follow_utils
from follow.models import Follow
from stream import utils as stream_utils

from shortcuts import DefaultCharField, DefaultDecimalField, DEFAULT_CHARFIELD_LENGTH


class UserProfile(models.Model):
    user = models.OneToOneField(User,
                                unique=True)
    location_lat = DefaultDecimalField(editable=False, blank=True, null=True)
    location_lon = DefaultDecimalField(editable=False, blank=True, null=True)
    location_address = DefaultCharField(blank=True, verbose_name='Местоположение')
    
    photo = models.ImageField(upload_to='user', null=True, blank=True, verbose_name='Фото')
    twitter = DefaultCharField(blank=True)
    
    def __unicode__(self):
        return "profile for %s" % self.user.username

    def is_following(self, obj):
        # FIXME django-follow docs recommend against calling this repeatedly
        return Follow.objects.is_following(self, obj)

    def get_absolute_url(self):
        return reverse('user_detail', kwargs={'username' : self.user.username})


class Collective(models.Model):
    # TODO should be related to a contrib.auth.models.Group for permissions
    name = DefaultCharField(verbose_name='Название')
    slug = models.SlugField(max_length=DEFAULT_CHARFIELD_LENGTH, verbose_name='Ярлык')

    location_lat = DefaultDecimalField(editable=False, blank=True, null=True)
    location_lon = DefaultDecimalField(editable=False, blank=True, null=True)
    location_address = DefaultCharField(blank=True, verbose_name='Место')
    
    description = models.TextField(verbose_name='Описание')
    twitter = DefaultCharField(blank=True)
    email = DefaultCharField(blank=True, verbose_name='Эл. почта')
    
    
    photo = models.ImageField(upload_to='collective', null=True, blank=True, verbose_name='Фото')

    members = models.ManyToManyField(User, related_name='collectives',
            null=True, blank=True)

    date_created = models.DateTimeField(default=timezone.now, editable=False)

    def __unicode__(self):
        return "%s (%d members)" % (self.name, self.members.count())

    def get_absolute_url(self):
        return reverse("collective_detail", kwargs={"slug": self.slug})


stream_utils.register_actor(User)
stream_utils.register_target(Collective)
stream_utils.register_action_object(Comment)

follow_utils.register(Collective)

from .signals import *
