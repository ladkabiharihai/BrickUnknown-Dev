from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=255)
    mob = models.CharField(max_length=12)
    comment = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
    

class gem(models.Model):
    Name = models.CharField(max_length=50)
    url = models.URLField(null=True)
    desc = models.TextField()
    special = models.TextField()
    image = models.ImageField(upload_to='home/images/gems/', default="")

    def __str__(self):
        return self.Name