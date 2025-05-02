from django.shortcuts import render,redirect
from .models import Test,TestAvailability
from .form import TestAvailabilityForm
from django.contrib.auth.decorators import login_required
# Create your views here.
# diagonostic_test/views.py
from django.shortcuts import render
from .models import TestAvailability, Test
from hospital.models import Hospital


def test_available_list(request):
    # Get filters from query
    test_name = request.GET.get('test_name')
    hospital_name = request.GET.get('hospital_name')
    city = request.GET.get('city')
    test_filter = request.GET.get('test_filter')

    # Start with all TestAvailability entries
    tests = TestAvailability.objects.all()

    # Apply filters
    if test_name:
        tests = tests.filter(test__name__icontains=test_name)

    if hospital_name:
        tests = tests.filter(hospital__name__icontains=hospital_name)

    if city:
        tests = tests.filter(hospital__city__iexact=city)

    if test_filter:
        tests = tests.filter(test__name__iexact=test_filter)

    # Send distinct dropdown values
    all_cities = Hospital.objects.values_list('city', flat=True).distinct()
    all_tests = Test.objects.values_list('name', flat=True).distinct()

    context = {
        'tests': tests,
        'all_cities': all_cities,
        'all_tests': all_tests,
    }
    return render(request, template_name='diagonostic_test/test_available_list.html', context = context )

@login_required
def upload_test(request):
    if request.method == 'POST':
        form = TestAvailabilityForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('test_available_list')
    else:
        form = TestAvailabilityForm()

    context = {'form': form}
    return render(request, template_name='diagonostic_test/upload_test.html', context=context)

@login_required
def update_test(request,id):
    test = TestAvailability.objects.get(pk=id)
    if request.method == 'POST':
        form = TestAvailabilityForm(request.POST, request.FILES,instance=test)
        if form.is_valid():
            form.save()
            return redirect('test_available_list')
    else:
        form = TestAvailabilityForm(instance=test)

    context = {'form': form}
    return render(request, template_name='diagonostic_test/upload_test.html', context=context)

@login_required
def delete_test(request,id):
    test=TestAvailability.objects.get(pk=id)
    if request.method == 'POST':
        test.delete()
        return redirect('test_available_list')
    return render(request, template_name='diagonostic_test/delete_test.html')

