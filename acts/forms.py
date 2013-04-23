# vim: fileencoding=utf-8 ai ts=4 sts=4 et sw=4
from django import forms

from bootstrap_toolkit.widgets import BootstrapDateInput

from .models import MikroAct, Campaign


class MikroActForm(forms.ModelForm):
    class Meta:
        model = MikroAct
        fields = ("title", "slug", "date", "description", "process", "location_address",
                  "is_published", "photo")
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
    campaign = forms.ModelChoiceField(queryset=Campaign.objects.all())
