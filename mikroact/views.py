# vim: fileencoding=utf-8 ai ts=4 sts=4 et sw=4
from django.shortcuts import render

# No need for relative import here as this is the overall site views.py
from acts.models import MikroAct, Campaign
from accounts.models import Collective


def home(request):
    mikro_acts = MikroAct.objects.filter(is_published=True)
    collectives = Collective.objects.filter()
    campaigns = Campaign.objects.filter()
    
    following = []

    return render(request, 'index.html', {
        'mikro_acts': mikro_acts,
        'collectives': collectives,
        'campaigns': campaigns,
        'following': following,
    })
    
