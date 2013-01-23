# vim: fileencoding=utf-8 ai ts=4 sts=4 et sw=4
from django.views.generic.detail import DetailView

from .models import Collection

class CollectionDetailView(DetailView):
    model = Collection
