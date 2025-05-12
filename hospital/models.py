from django.db import models


# Create your models here.
#hospital info
class Hospital(models.Model):
    name = models.CharField(max_length=200 ,blank= True,null=True)
    profile_pic = models.ImageField(upload_to='doc_img/',blank=True, null=True)
    address = models.CharField(max_length=200 ,blank= True,null=True)
    city = models.CharField(max_length=100,blank= True,null=True)
    hotline = models.CharField(max_length=20,blank= True,null=True)
    email = models.EmailField(blank=True,null=True)

    def __str__(self):
        return self.name





