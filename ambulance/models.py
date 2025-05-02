from django.db import models
from django.conf import settings

# Create your models here.
#driver info admin dekhte parbe shudhu
class Driver(models.Model):
    name = models.TextField(blank=True,null= True)
    profile_pic = models.ImageField(upload_to='doc_img/', blank=True, null=True)
    age = models.IntegerField(blank=True,null= True)
    salary = models.IntegerField(blank=True,null= True)
    is_available = models.BooleanField(default=True)
    def __str__(self):
        return self.name


#ambulance info admin dekhbe
class Ambulance(models.Model):

    driver = models.ForeignKey(Driver, on_delete=models.CASCADE,blank= True,null=True)
    contact_number = models.CharField(max_length=20)
    is_available = models.BooleanField(default=True)
    def __str__(self):
        return f"Ambulance - {self.driver.name if self.driver else 'No Driver'}"


class AmbulanceRequest(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    ambulance = models.ForeignKey(Ambulance, on_delete=models.CASCADE, blank=True, null=True)
    from_address = models.TextField(blank=True, null=True)
    to_address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)

    status_choice = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('completed', 'Completed'),
    ]
    status = models.CharField(max_length=100, choices=status_choice, blank=True, null=True,default='pending')

    def __str__(self):
        return self.user.get_full_name() or self.user.username




