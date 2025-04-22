from django.db import models
from django.contrib.auth.models import User
from doctors.models import Doctor
# Create your models here.

#appointment
class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE,blank=True,null= True)
    user= models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null= True)
    patient_name = models.CharField(max_length=100,blank=True,null= True)
    age = models.IntegerField(blank=True,null= True)
    gender = models.CharField(max_length=10,blank=True,null= True)
    birth_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    contact_info = models.CharField(max_length=100,blank=True,null= True)
    appointment_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    status_choice = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),

    ]
    status = models.CharField(max_length=100, choices = status_choice, blank=True, null=True)

    def __str__(self):
        return f"{self.patient_name} - {self.doctor.name}"