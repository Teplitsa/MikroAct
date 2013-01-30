# vim: fileencoding=utf-8 ai ts=4 sts=4 et sw=4
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse

from guardian.mixins import LoginRequiredMixin

from .models import Collective


class CollectiveListView(ListView):
    model = Collective


class CollectiveCreateView(CreateView):
    model = Collective


class CollectiveUpdateView(UpdateView):
    model = Collective


class CollectiveDetailView(DetailView):
    model = Collective


class CollectiveJoinView(LoginRequiredMixin, View, SingleObjectMixin):
    model = Collective

    def post(self, request, *args,  **kwargs):
        self.object = self.get_object()

        self.object.members.add(request.user)

        return HttpResponseRedirect(self.object.get_absolute_url())

    def head(self, request, *args, **kwargs):                                   
        return self.post(request, *args, **kwargs)                               
                                                                                
    def get(self, request, *args, **kwargs):                                   
        return self.post(request, *args, **kwargs)                               
                                                                                
    def options(self, request, *args, **kwargs):                                
        return self.post(request, *args, **kwargs)                               
                                                                                
    def delete(self, request, *args, **kwargs):                                 
        return self.post(request, *args, **kwargs)                               
                                                                                
    def put(self, request, *args, **kwargs):                                    
        return self.post(request, *args, **kwargs)    
