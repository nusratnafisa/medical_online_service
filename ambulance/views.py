from django.shortcuts import render
from .models import Driver,Ambulance,AmbulanceRequest
# Create your views here.
def ambulance_req(request):
    AmbulanceRequests = AmbulanceRequest.objects.all()
    context = {
        'AmbulanceRequests': AmbulanceRequests
    }
    return render(request,template_name='ambulance/ambulance_req.html',context = context)