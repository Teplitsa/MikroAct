# vim: fileencoding=utf-8 ai ts=4 sts=4 et sw=4
from django import forms

from .models import MikroAct


class MikroActForm(forms.ModelForm):
    class Meta:
        model = MikroAct
        fields = ("title", "slug", "date", "description", "location_address",
                  "status", "is_published", "photo")
