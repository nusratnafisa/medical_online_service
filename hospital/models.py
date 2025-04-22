from django.db import models


# Create your models here.
#hospital info
class Hospital(models.Model):
    name = models.TextField(blank= True,null=True)
    address = models.TextField(blank= True,null=True)
    city = models.CharField(max_length=100,blank= True,null=True)
    hotline = models.CharField(max_length=20,blank= True,null=True)
    email = models.EmailField(blank= True,null=True)

    def __str__(self):
        return self.name





