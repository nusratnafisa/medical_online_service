from django.shortcuts import render
from .models import Test,TestAvailability
# Create your views here.
def test_available_list(request):
    tests= TestAvailability.objects.all()
    context = {
        'tests': tests
    }
    return render(request,template_name='diagonostic_test/test_available_list.html',context=context)
def test_info(request):

    return render(request,template_name='diagonostic_test/test_info.html')