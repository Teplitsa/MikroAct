from django.contrib import admin

from .models import MikroAct, Collection, CollectionMembership

class CollectionMembershipInline(admin.TabularInline):
	model = CollectionMembership

class CollectionAdmin(admin.ModelAdmin):
	inlines = [
			CollectionMembershipInline,
	]

admin.site.register(MikroAct)
admin.site.register(Collection, CollectionAdmin)
