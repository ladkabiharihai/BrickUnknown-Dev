from django.urls import path
from . import views


urlpatterns = [
path('', views.index, name='project'),
path('createproject',views.createProject,name='createProject'),
]