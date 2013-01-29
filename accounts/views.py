# vim: fileencoding=utf-8 ai ts=4 sts=4 et sw=4
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from .models import Collective


class CollectiveListView(ListView):
    model = Collective


class CollectiveCreateView(CreateView):
    model = Collective


class CollectiveUpdateView(UpdateView):
    model = Collective


class CollectiveDetailView(DetailView):
    model = Collective
