# vim: fileencoding=utf-8 ai ts=4 sts=4 et sw=4
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from .models import Collection, MikroAct
from .forms import MikroActForm


class CollectionListView(ListView):
    model = Collection


class CollectionCreateView(CreateView):
    model = Collection


class CollectionUpdateView(UpdateView):
    model = Collection


class CollectionDetailView(DetailView):
    model = Collection


class MikroActListView(ListView):
    model = MikroAct


class MikroActCreateView(CreateView):
    model = MikroAct
    form_class = MikroActForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super (MikroActCreateView, self).form_valid(form)

class MikroActUpdateView(UpdateView):
    model = MikroAct


class MikroActDetailView(DetailView):
    model = MikroAct
