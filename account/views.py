from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .form import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

@login_required
def user_profile(request):
    return render(request,template_name='account/user_profile.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')  # After successful login, go to home
        else:
            error = 'Invalid username or password'
            context =  {'error': error}
            return render(request, template_name='account/login.html',context= context)
    return render(request, template_name='account/login.html')



def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to homepage
    else:
        form = CustomUserCreationForm()

    return render(request, template_name='account/register.html', context = {'form': form})


def term_condition(request):
    return render(request, template_name='help/term_condition.html')
def privacy_policy(request):
    return render(request, template_name='help/privacy_policy.html')