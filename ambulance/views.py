from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .form import AmbulanceRequestForm
from .models import Ambulance, AmbulanceRequest

@login_required
def ambulance_req(request):
    if request.method == 'POST':
        form = AmbulanceRequestForm(request.POST)
        if form.is_valid():
            ambulance_request = form.save(commit=False)
            ambulance_request.user = request.user

            # Try assigning available ambulance and driver
            ambulance = Ambulance.objects.filter(is_available=True, driver__is_available=True).first()

            if ambulance:
                ambulance_request.ambulance = ambulance
                ambulance_request.status = 'accepted'

                ambulance.is_available = False
                ambulance.driver.is_available = False

                ambulance.save()
                ambulance.driver.save()
                ambulance_request.save()
                return redirect('ambulance_req_success')
            else:
                ambulance_request.status = 'pending'
                ambulance_request.save()
                return redirect('ambulance_req_success')
    else:
        form = AmbulanceRequestForm()

    return render(request, template_name='ambulance/ambulance_req.html', context={'form': form})


@login_required
def complete_ambulance_request(request, id):
    ambulance_request = AmbulanceRequest.objects.get( pk=id, user=request.user,status='accepted')

    if ambulance_request.status != 'completed':
        ambulance_request.status = 'completed'
        ambulance_request.save()

        ambulance = ambulance_request.ambulance
        if ambulance:
            ambulance.is_available = True
            ambulance.save()

            if ambulance.driver:
                ambulance.driver.is_available = True
                ambulance.driver.save()

    return redirect('ambulance_req')  # or another page


@login_required
def ambulance_req_success(request):
    return render(request, template_name='ambulance/ambulance_req_success.html')
@login_required
def user_ambulance_requests(request):
    user_requests = AmbulanceRequest.objects.filter(user=request.user).order_by('-date')
    return render(request, template_name='ambulance/user_requests.html', context={'requests': user_requests})