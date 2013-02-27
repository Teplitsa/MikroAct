# vim: fileencoding=utf-8 ai ts=4 sts=4 et sw=4
from django import forms
from django.contrib.auth.models import User

from .models import UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), 
                                label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput(), 
                                label="Confirm password")

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
