from django.contrib import admin
from django.contrib.auth.models import Permission

from .models import Collective, UserProfile

admin.site.register(Collective)
admin.site.register(UserProfile)
admin.site.register(Permission)
