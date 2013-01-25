from django.contrib import admin

from .models import Collective, CollectiveMembership

class CollectiveMembershipInline(admin.TabularInline):
	model = CollectiveMembership

class CollectiveAdmin(admin.ModelAdmin):
	inlines = [
			CollectiveMembershipInline,
	]

admin.site.register(Collective, CollectiveAdmin)
