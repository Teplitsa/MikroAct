# vim: fileencoding=utf-8 ai ts=4 sts=4 et sw=4
from django import forms
from django.contrib.auth.models import User

from .models import UserProfile, Collective


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)


class RegistrationForm(UserForm):
    password = forms.CharField(widget=forms.PasswordInput(), label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput(), 
                                label="Confirm password")

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')

    def clean_password2(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")

        if password and password2 and password != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        if self.cleaned_data.get('password', False):
            user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("location_address", "twitter", "photo")


class CollectiveForm(forms.ModelForm):
    class Meta:
        model = Collective
        fields = ('name', 'slug', 'description', 'location_address', 'twitter',
                  'email', 'photo')
        widgets = {
            "slug": forms.TextInput(attrs={"data-slug-from": "name"}),
        }


class CollectiveUserPromotionForm(forms.Form):
    users = forms.ModelMultipleChoiceField(
        queryset=User.objects.none(),
        widget=forms.CheckboxSelectMultiple
    )

    def __init__(self, *args, **kwargs):
        self.collective = kwargs.pop('collective', False)

        if self.collective:
            self.base_fields['users'].queryset = User.objects.filter(
                following__target_collective=self.collective
            ).exclude(collectives=self.collective)

        return super(CollectiveUserPromotionForm, self).__init__(*args, **kwargs)
    
    def save(self):
        data = self.cleaned_data

        self.collective.members.add(*data['users'])

        return data['users']
