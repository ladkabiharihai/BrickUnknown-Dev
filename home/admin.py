from django.contrib import admin

# Register your models here.
from home.models import Contact,gem

class contactAdmin(admin.ModelAdmin):
    list_display = ('name','mob','email','date')
    search_fields = ('email','mob')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()



admin.site.register(Contact,contactAdmin)
admin.site.register(gem)
