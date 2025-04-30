from django.db import models
from django.conf import settings
from doctors.models import Doctor
# Create your models here.

#appointment
class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE,blank=True,null= True)
    user= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,blank=True,null= True)
    patient_name = models.CharField(max_length=100,blank=True,null= True)
    age = models.IntegerField(blank=True,null= True)
    gender = models.CharField(max_length=10,blank=True,null= True)
    birth_date = models.DateField(blank=True,null= True)
    contact_info = models.CharField(max_length=100,blank=True,null= True)
    appointment_date = models.DateField(blank=True,null= True)
    status_choice = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),

    ]
    status = models.CharField(max_length=100, choices = status_choice, blank=True, null=True)

    def __str__(self):
        doctor_name = self.doctor.name if self.doctor else 'No Doctor Assigned'
        return f"{self.patient_name} - {doctor_name}"