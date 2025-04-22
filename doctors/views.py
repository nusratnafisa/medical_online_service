from django.shortcuts import render
from .models import Doctor,Dept
# Create your views here.
def home(request):
    return render(request,template_name='doctors\home.html')
def doc_search(request):
    return render(request,template_name='doctors\doc_search.html')
def doctor_list(request):
    doctors = Doctor.objects.all()
    context = {
        'doctors': doctors
    }
    return render(request,template_name='doctors\doctor_list.html', context=context)



