from django.contrib import admin

# Register your models here.
from blog.models import BlogPost

class blogAdmin(admin.ModelAdmin):
    list_display = ('author','title','date_updated')
    search_fields = ('title','author')
    list_filter = ('author', 'title')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(BlogPost,blogAdmin)
