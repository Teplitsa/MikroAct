# vim: fileencoding=utf-8 ai ts=4 sts=4 et sw=4
from django import forms

from bootstrap_toolkit.widgets import BootstrapDateInput
from guardian.shortcuts import get_objects_for_user

from .models import MikroAct, Campaign


class MikroActForm(forms.ModelForm):
    class Meta:
        model = MikroAct
        fields = ("title", "slug", "date", "description", "process", "location_address",
                  "photo")
        widgets = {
            "slug": forms.TextInput(attrs={"data-slug-from": "title"}),
            "date": BootstrapDateInput()
        }


class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ("name", "slug", "description", "is_private")
        widgets = {
            "slug": forms.TextInput(attrs={"data-slug-from": "name"}),
        }


class AddToCampaignForm(forms.Form):
    campaign = forms.ModelChoiceField(queryset=Campaign.objects.none())

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', False)
        if user and user.is_authenticated():
            self.base_fields['campaign'].queryset = get_objects_for_user(
                user, 'acts.change_campaign', Campaign)
        return super(AddToCampaignForm, self).__init__(*args, **kwargs)
