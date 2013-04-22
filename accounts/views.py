# vim: fileencoding=utf-8 ai ts=4 sts=4 et sw=4
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.views.generic import View, TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse

from guardian.mixins import LoginRequiredMixin, PermissionRequiredMixin
from guardian.shortcuts import assign

from .models import Collective, UserProfile
from .forms import UserForm, UserProfileForm, RegistrationForm


class CollectiveListView(ListView):
    model = Collective


class CollectiveCreateView(PermissionRequiredMixin, CreateView):
    permission_required = "accounts.add_collective"
    model = Collective


    # guardian's PermissionRequiredMixin doesn't like CreateView, which doesn't
    # indicate that there is no associated model (yet) very meaningfully
    object = None
    def get_object(self):
        return None

    def form_valid(self, form):
        collective = form.save(commit=False)
        collective.save()

        self.object = collective

        assign("change_collective", self.request.user, collective)
        assign("delete_collective", self.request.user, collective)

        return HttpResponseRedirect(self.get_success_url())


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

    form_class = RegistrationForm
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
    

class UserListView(ListView):
    model = UserProfile
    template_name = "accounts/user_list.html"
      
    
class UserDetailView(DetailView):
    model = UserProfile
    template_name = "accounts/user_detail.html"
    
    def get_object(self):
    	try:
    		return UserProfile.objects.get(user__username=self.kwargs['username'])
    	except UserProfile.DoesNotExist:
    		user = User.objects.get(username = self.kwargs['username'])
    		userprofile = UserProfile.objects.create(user=user)
    		assign("change_userprofile", user, userprofile)
    		return userprofile


class UserUpdateView(PermissionRequiredMixin, UpdateView):
    model = UserProfile
    permission_required = "accounts.change_userprofile"
    
    slug_field = "user__username"
    slug_url_kwarg = "username"
    template_name = "accounts/user_form.html"
    form_class = UserProfileForm
    
    def get_form(self, form_class):
    	if self.request.method == 'POST' :
    		self.userform = UserForm(self.request.POST, instance = self.object.user)
    	else:
    		self.userform = UserForm(instance = self.object.user)
    	
    	return super(UserUpdateView, self).get_form(form_class)
    	
    def get_context_data(self, **kwargs):
    	kwargs['user_form'] = self.userform
    	return super(UserUpdateView, self).get_context_data(**kwargs)
    	
    def form_valid(self, form):
    	userprofile = form.save(commit=False)
    	if self.userform.is_valid():
    		userprofile.save()
    		self.userform.save()
    		
    		return HttpResponseRedirect(self.get_success_url())
    	
    	# import pdb; pdb.set_trace()
    	return self.form_invalid(form)
    	
    
