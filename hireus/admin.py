from django.contrib import admin
from django.contrib.auth.admin import User

# Register your models here.
from hireus.models import *

class productAdmin(admin.ModelAdmin):
    list_display = ('Product_name','category','pub_date')
    search_fields = ('category','Product_name')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()



class bookedAdmin(admin.ModelAdmin):
    list_display = ('name','mob','email','category','Product_name','date')
    search_fields = ('email','mob','category')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Product,productAdmin)
admin.site.register(booked,bookedAdmin)
