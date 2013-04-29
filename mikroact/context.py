# vim: fileencoding=utf-8 ai ts=4 sts=4 et sw=4
from django.db.models import Q

from follow.models import Follow
from stream.models import Action

def stream(request):
    if not request.user.is_authenticated():
        return {}

    following = Follow.objects.filter(user=request.user)

    stream = list(Action.objects.filter(
        Q(target_campaign_id__in=following.values_list('target_campaign'))
        | Q(target_collective_id__in=following.values_list('target_collective'))
        | Q(actor_user=request.user)
    ).order_by('-datetime')[:30])

    # sqlite doesn't support DISTINCT ON (..), so we make our own in Python
    stream_keys = []
    stream_list = []
    while len(stream_keys) < 20 and len(stream) > 0:
        o = stream.pop()
        keys = (o.target_mikroact, o.target_campaign, o.target_collective,
                o.actor_user, o.verb)
        if keys not in stream_keys:
            stream_keys.append(keys)
            stream_list.append(o)

    return {
        'stream': stream_list
    }
