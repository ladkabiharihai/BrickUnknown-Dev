from django.db import models
from django.conf import settings
# Create your models here.

class project(models.Model):
    ProjectId = models.AutoField(primary_key=True)
    ProjectName = models.CharField(max_length=50)
    Owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category1 = models.CharField(max_length=50)
    category2 = models.CharField(max_length=50, blank=True)
    category3 = models.CharField(max_length=50, blank=True)
    category4 = models.CharField(max_length=50, blank=True)
    category5 = models.CharField(max_length=50, blank=True)
    link = models.URLField(unique=True)
    github = models.URLField()
    linedin = models.URLField()
    desc = models.TextField()
    pub_date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='project/images', default="")

    def __str__(self):
        return self.ProjectName