from django.contrib import admin
from .models  import  Test,TestAvailability

# Register your models here.
admin.site.register([Test,TestAvailability])
