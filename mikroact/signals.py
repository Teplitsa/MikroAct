# vim: fileencoding=utf-8 ai ts=4 sts=4 et sw=4
from django.contrib.comments.models import Comment
from django.contrib.comments.signals import comment_was_posted
from django.dispatch import receiver

from stream import utils as stream_utils


@receiver(comment_was_posted, sender=Comment)
def comment_action(sender, comment, request, **kwargs):
    stream_utils.action.send(comment.user, 'commented', comment.content_object,
                             comment)
