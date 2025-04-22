from django.shortcuts import render
from .models import Hospital

# Create your views here.
def hospital_info(request):
    return render(request,template_name='hospital\hospital_info.html')
def hospital_list(request):
    Hospitals = Hospital.objects.all()
    context = {
        'Hospitals': Hospitals
    }
    return render(request,template_name='hospital\hospital_list.html',context= context)