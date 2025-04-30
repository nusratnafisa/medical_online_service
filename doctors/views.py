from django.shortcuts import render
from .models import Doctor,Dept
# Create your views here.
def home(request):
    return render(request,template_name='doctors\home.html')

def doctor_list(request):
    doctors = Doctor.objects.all()

    # Get search query parameters
    doctor_name = request.GET.get('doctor_name')
    hospital_name = request.GET.get('hospital_name')
    city = request.GET.get('city')
    speciality = request.GET.get('speciality')
    gender = request.GET.get('gender')

    # Filter based on search
    if doctor_name:
        doctors = doctors.filter(name__icontains=doctor_name)

    if hospital_name:
        doctors = doctors.filter(hospitals__name__icontains=hospital_name)

    if city:
        doctors = doctors.filter(city__iexact=city)

    if speciality:
        doctors = doctors.filter(dept__dept_name__iexact=speciality)

    if gender:
        doctors = doctors.filter(gender__iexact=gender)

    # To send city and department choices to template
    all_cities = Doctor.objects.values_list('city', flat=True).distinct()
    all_specialities = Dept.objects.values_list('dept_name', flat=True).distinct()

    context = {
        'doctors': doctors,
        'all_cities': all_cities,
        'all_specialities': all_specialities,
        'search_data': {
            'doctor_name': doctor_name,
            'hospital_name': hospital_name,
            'city': city,
            'speciality': speciality,
            'gender': gender,
        }
    }
    return render(request, template_name='doctors/doctor_list.html', context=context)