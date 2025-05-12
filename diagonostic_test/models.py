from django.db import models
from hospital.models import Hospital
# Create your models here.
#test info
class Test(models.Model):
    name = models.CharField(max_length=100,blank=True, null= True)
    description = models.CharField(max_length=100, blank=True, null=True)

                                   
    # Many-to-Many with Hospital using TestAvailability as a middle table
    hospital = models.ManyToManyField(Hospital, through='TestAvailability')
    def __str__(self):
        return self.name

# One test can be available in many hospitals, and one hospital can offer many tests
# But I also want to store more info about each test at each hospital (like price, availability).
# So I’ll use a middle table called TestAvailability to connect them.

#test list a show korbe
class TestAvailability(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE,blank=True, null= True)
    test = models.ForeignKey(Test, on_delete=models.CASCADE,blank=True, null= True)
    price = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null= True)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.hospital.name} - {self.test.name}"
