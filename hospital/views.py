from django.shortcuts import render,redirect
from .models import Hospital
from .form import HospitalForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def hospital_list(request):
    hospitals = Hospital.objects.all()

    # Get search query parameters
    hospital_name = request.GET.get('hospital_name')
    city = request.GET.get('city')

    # Apply filters
    if hospital_name:
        hospitals = hospitals.filter(name__icontains=hospital_name)

    if city:
        hospitals = hospitals.filter(city__iexact=city)

    # Get all unique cities for dropdown
    all_cities = Hospital.objects.values_list('city', flat=True).distinct()

    context = {
        'hospitals': hospitals,
        'all_cities': all_cities,
    }
    return render(request, template_name='hospital/hospital_list.html', context= context)


def hospital_info(request, id):
    hospitals = Hospital.objects.get(pk=id)

    context = {
        'hospitals': hospitals
    }
    return render(request, template_name='hospital\hospital_info.html',context = context )

@login_required
def upload_hospital(request):
    if request.method == 'POST':
        form = HospitalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('hospital_list')
    else:
        form = HospitalForm()

    context = {'form': form}
    return render(request, template_name='hospital/upload_hospital.html', context=context)

@login_required
def update_hospital(request,id):
    hospital= Hospital.objects.get(pk=id)
    if request.method == 'POST':
        form = HospitalForm(request.POST, request.FILES,instance=hospital)
        if form.is_valid():
            form.save()
            return redirect('hospital_list')
    else:
        form = HospitalForm(instance=hospital)

    context = {'form': form}
    return render(request, template_name='hospital/upload_hospital.html', context=context)

@login_required
def delete_hospital(request,id):
    hospital= Hospital.objects.get(pk=id)
    if request.method == 'POST':
        hospital.delete()
        return redirect('hospital_list')
    return render(request, template_name='hospital/delete_hospital.html')