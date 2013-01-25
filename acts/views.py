# vim: fileencoding=utf-8 ai ts=4 sts=4 et sw=4
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from .models import Collection


class CollectionListView(ListView):
    model = Collection


class CollectionCreateView(CreateView):
    model = Collection


class CollectionDetailView(DetailView):
    model = Collection
