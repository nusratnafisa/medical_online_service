from django.db import models


# Create your models here.

# doctor profile e show korbe
# doctor list show korbe db table doctor
class Doctor(models.Model):
    name = models.CharField(max_length=200 ,blank=True, null=True)
    profile_pic = models.ImageField(upload_to='doc_img/',blank=True,null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    education = models.CharField(max_length=200 ,blank=True, null=True)  # institution name jekhane poralikha korse
    specialization = models.CharField(max_length=200 ,blank=True, null=True)
    Profession = models.CharField(max_length=200 ,blank=True, null=True)
    chamber_address = models.CharField(max_length=200 ,blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)


    # Related hospitals through Dept model
    hospitals = models.ManyToManyField('hospital.Hospital', through='Dept')
    def __str__(self):
        return self.name




class Dept(models.Model):
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE)
    hospital = models.ForeignKey('hospital.Hospital', on_delete=models.CASCADE)
    dept_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.hospital.name} - {self.dept_name}"



