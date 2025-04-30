# appointment/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .form import AppointmentForm
from doctors.models import Doctor
from .models import Appointment

@login_required
def book_appointment(request,id ):
    doctor = Doctor.objects.get(pk= id)

    if request.method == 'POST':
        form = AppointmentForm(request.POST,request.FILES)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.doctor = doctor
            appointment.user = request.user  # Save the logged-in user
            appointment.save()
            return redirect('doctor_list')
    else:
        form = AppointmentForm()

    context = {
        'form': form,
        'doctor': doctor
    }
    return render(request,template_name='doctors/book_appointment.html', context= context)
