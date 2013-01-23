from django.contrib import admin
from model.models import Twitters, Garbage

class TwittersAdmin(admin.ModelAdmin):
    list_display = ('screen_name', 'text', )
    search_fields = ('new',)
    fields = ('aprove', 'new', )

class GarbageAdmin(admin.ModelAdmin):
	list_display = ('uid', 'twid', )


admin.site.register(Twitters, TwittersAdmin)
admin.site.register(Garbage, GarbageAdmin)
