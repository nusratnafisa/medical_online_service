from django.shortcuts import render
from .models import Appointment
# Create your views here.
def book_appointment(request):
    Appointments = Appointment.objects.all()
    context = {
        'Appointments': Appointments
    }
    return render(request,template_name='doctors/book_appointment.html',context = context)