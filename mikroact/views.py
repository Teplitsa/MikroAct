# vim: fileencoding=utf-8 ai ts=4 sts=4 et sw=4
from django.db.models import Q
from django.shortcuts import render

from follow.models import Follow
from stream.models import Action

# No need for relative import here as this is the overall site views.py
from acts.models import MikroAct


def home(request):
    mikro_acts = MikroAct.objects.filter(is_published=True)

    following = []
    stream = []

    if request.user.is_authenticated():
        following = Follow.objects.filter(user=request.user)
        stream = Action.objects.filter(
            Q(target_campaign_id__in=following.values_list('target_campaign'))
            | Q(actor_user=request.user)
        ).order_by('-datetime')[0:20]

    return render(request, 'index.html', {
        'mikro_acts': mikro_acts,
        'following': following,
        'stream': stream,
    })
