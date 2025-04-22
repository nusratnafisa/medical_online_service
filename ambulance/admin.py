
from django.contrib import admin
from .models  import  Driver,Ambulance,AmbulanceRequest

# Register your models here.
admin.site.register([Driver,Ambulance,AmbulanceRequest])

