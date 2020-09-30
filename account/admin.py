from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from account.models import Account


class AccountAdmin(UserAdmin):
    list_display = ('email','username','full_name','date_joined','last_login','is_admin','is_staff','is_mentor')
    search_fields = ('email','username')
    readonly_fields = ('date_joined','last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()





admin.site.register(Account, AccountAdmin)

