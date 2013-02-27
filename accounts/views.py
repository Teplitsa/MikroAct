# vim: fileencoding=utf-8 ai ts=4 sts=4 et sw=4
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.views.generic import View, TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse

from guardian.mixins import LoginRequiredMixin

from .models import Collective
from .forms import UserForm, UserProfileForm


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


class UserRegisterView(CreateView):
    model = User

    form_class = UserForm
    template_name = "accounts/user_register.html"

    def get_success_url(self):
        return reverse('user_register_done')

    def form_valid(self, form):
        user = form.save(commit=False)

        # FIXME uncomment when (if) we add email activation
        # user.is_active = False

        user.save()

        user.backend='django.contrib.auth.backends.ModelBackend'
        login(self.request, user)

        # FIXME send "activate" email here

        return HttpResponseRedirect(self.get_success_url())


class UserRegisterCompleteView(TemplateView):
    template_name = "accounts/user_register_done.html"
