from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="blog"),
    path("create",views.create_blog,name="create"),
    path("<slug>/",views.detail_blog_view,name="detail"),
    path("<slug>/edit",views.edit_blog_view,name="edit"),
]    
