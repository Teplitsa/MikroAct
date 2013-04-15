from django.contrib import admin

from .models import Collective, UserProfile

admin.site.register(Collective)
admin.site.register(UserProfile)
