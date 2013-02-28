# vim: fileencoding=utf-8 ai ts=4 sts=4 et sw=4
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.views.generic.edit import CreateView, UpdateView

from follow import utils as follow_utils
from stream import utils as stream_utils
from guardian.mixins import PermissionRequiredMixin, LoginRequiredMixin
from guardian.shortcuts import assign

from .models import List, MikroAct
from .forms import MikroActForm, ListForm


class ListListView(ListView):
    model = List


class ListCreateView(PermissionRequiredMixin, CreateView):
    permission_required = "acts.add_list"
    model = List

    form_class = ListForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(ListCreateView, self).form_valid(form)

    # guardian's PermissionRequiredMixin doesn't like CreateView, which doesn't
    # indicate that there is no associated model (yet) very meaningfully
    object = None
    def get_object(self):
        return None


class ListUpdateView(PermissionRequiredMixin, UpdateView):
    model = List
    permission_required = "acts.change_list"
    form_class = ListForm


class ListDetailView(DetailView):
    model = List


class ListFollowView(LoginRequiredMixin, View, SingleObjectMixin):
    model = List

    def post(self, request, *args,  **kwargs):
        self.object = self.get_object()

        follow_utils.follow(request.user, self.object)

        return HttpResponseRedirect(reverse("list_detail", 
                                    kwargs={"slug": self.object.slug}))

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


class MikroActListView(ListView):
    model = MikroAct


class MikroActCreateView(PermissionRequiredMixin, CreateView):
    model = MikroAct
    form_class = MikroActForm
    permission_required = "acts.add_mikroact"

    # guardian's PermissionRequiredMixin doesn't like CreateView, which doesn't
    # indicate that there is no associated model (yet) very meaningfully
    object = None
    def get_object(self):
        return None

    def form_valid(self, form):
        mikroact = form.save(commit=False)
        mikroact.author = self.request.user
        mikroact.save()

        self.object = mikroact

        assign("change_mikroact", self.request.user, mikroact)
        assign("delete_mikroact", self.request.user, mikroact)

        return HttpResponseRedirect(self.get_success_url())



class MikroActUpdateView(PermissionRequiredMixin, UpdateView):
    model = MikroAct
    form_class = MikroActForm
    permission_required = "acts.change_mikroact"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(MikroActCreateView, self).form_valid(form)


class MikroActDetailView(DetailView):
    model = MikroAct
