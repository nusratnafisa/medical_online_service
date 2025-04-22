from django.shortcuts import render

# Create your views here.
def user_profile(request):
    return render(request,template_name='account/user_profile.html')
def login(request):
    return render(request,template_name='account/login.html')
def register(request):
    return render(request,template_name='account/register.html')