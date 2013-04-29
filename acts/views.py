# vim: fileencoding=utf-8 ai ts=4 sts=4 et sw=4
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from follow import utils as follow_utils
from stream.models import Action
from stream import utils as stream_utils
from guardian.mixins import PermissionRequiredMixin, LoginRequiredMixin
from guardian.shortcuts import assign

from .models import Campaign, MikroAct
from .forms import MikroActForm, CampaignForm, AddToCampaignForm


class CampaignListView(ListView):
    model = Campaign


class CampaignCreateView(PermissionRequiredMixin, CreateView):
    permission_required = "acts.add_campaign"
    model = Campaign

    form_class = CampaignForm

    # guardian's PermissionRequiredMixin doesn't like CreateView, which doesn't
    # indicate that there is no associated model (yet) very meaningfully
    object = None
    def get_object(self):
        return None

    def form_valid(self, form):
        campaign = form.save(commit=False)
        campaign.author = self.request.user
        campaign.save()

        self.object = campaign

        stream_utils.action.send(self.request.user, 'created', self.object)

        assign("change_campaign", self.request.user, campaign)
        assign("delete_campaign", self.request.user, campaign)

        return HttpResponseRedirect(self.get_success_url())


class CampaignUpdateView(PermissionRequiredMixin, UpdateView):
    model = Campaign
    permission_required = "acts.change_campaign"
    form_class = CampaignForm

    def form_valid(self, form):
        campaign = form.save()
        
        self.object = campaign

        stream_utils.action.send(self.request.user, 'edited', self.object)

        return HttpResponseRedirect(self.get_success_url())


class CampaignDetailView(DetailView):
    model = Campaign

    def get_context_data(self, **kwargs):
        kwargs['object_stream'] = Action.objects.filter(
            Q(target_campaign=self.object) |
            Q(target_mikroact__in=self.object.mikro_acts.all())
        ).order_by('-datetime')
        return super(CampaignDetailView, self).get_context_data(**kwargs)


class CampaignFollowView(LoginRequiredMixin, View, SingleObjectMixin):
    model = Campaign

    def post(self, request, *args,  **kwargs):
        self.object = self.get_object()

        follow_utils.follow(request.user, self.object)
        stream_utils.action.send(request.user, 'followed', self.object)

        return HttpResponseRedirect(reverse("campaign_detail", 
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


class CampaignUnFollowView(CampaignFollowView):
    def post(self, request, *args,  **kwargs):
        self.object = self.get_object()

        follow_utils.unfollow(request.user, self.object)

        return HttpResponseRedirect(reverse("campaign_detail", 
                                    kwargs={"slug": self.object.slug}))


class MikroActListView(ListView):
    model = MikroAct
    
    def get_context_data(self, **kwargs):
        kwargs.setdefault('campaign_form', AddToCampaignForm())
        return super(MikroActListView, self).get_context_data(**kwargs)

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

        stream_utils.action.send(self.request.user, 'created', self.object)

        # TODO should this be in MikroActForm.save, or even MikroAct.save()?
        assign("change_mikroact", self.request.user, mikroact)
        assign("delete_mikroact", self.request.user, mikroact)

        return HttpResponseRedirect(self.get_success_url())


class MikroActUpdateView(PermissionRequiredMixin, UpdateView):
    model = MikroAct
    form_class = MikroActForm
    permission_required = "acts.change_mikroact"

    def form_valid(self, form):
        self.object = form.save()

        stream_utils.action.send(self.request.user, 'edited', self.object)

        return HttpResponseRedirect(self.get_success_url())


class MikroActDeleteView(PermissionRequiredMixin, DeleteView):
    model = MikroAct
    permission_required = "acts.delete_mikroact"

    def get_success_url(self):
        return reverse("mikroact_list")


class MikroActDetailView(DetailView):
    model = MikroAct

    def get_context_data(self, **kwargs):
        kwargs.setdefault('campaign_form', AddToCampaignForm())
        return super(MikroActDetailView, self).get_context_data(**kwargs)


class MikroActCampaignView(DetailView, FormView):
    model = MikroAct
    form_class = AddToCampaignForm

    def get(self, *args, **kwargs):
        return HttpResponseRedirect(reverse('mikroact_detail', kwargs={
            'slug': kwargs['slug']
        }))

    def form_valid(self, form):
        self.object = self.get_object()

        campaign = form.cleaned_data.get('campaign')
        campaign.mikro_acts.add(self.object)

        stream_utils.action.send(self.request.user, 'added', self.object, campaign)

        return self.get(slug=self.object.slug)
