"""
URL configuration for medical_online_service project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from . import settings
from django.conf.urls.static import static
from django.urls import path
from account import views as a_views
from doctors import views as d_views
from appointment import views as ap_views
from hospital import views as h_views
from ambulance import views as am_views
from diagonostic_test import views as dt_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user_profile/',a_views.user_profile,name='user_profile'),
    path('login/', a_views.user_login, name='login'),
    path('logout/', a_views.user_logout, name='logout'),
    path('register/', a_views.register, name='register'),
    path('term_condition/', a_views.term_condition, name='term_condition'),
    path('privacy_policy/', a_views.privacy_policy, name='privacy_policy'),
    path('', d_views.home, name='home'),
    path('doctor_list/', d_views.doctor_list, name='doctor_list'),
    path('upload_doctor/', d_views.upload_doctor, name='upload_doctor'),
    path('update_doctor/<str:id>', d_views.update_doctor, name='update_doctor'),
    path('delete_doctor/<str:id>', d_views.delete_doctor, name='delete_doctor'),
    path('book_appointment/<str:id>', ap_views.book_appointment, name='book_appointment'),
    path('hospital_list/', h_views.hospital_list, name='hospital_list'),
    path('upload_hospital/', h_views.upload_hospital, name='upload_hospital'),
    path('update_hospital/<str:id>', h_views.update_hospital, name='update_hospital'),
    path('delete_hospital/<str:id>', h_views.delete_hospital, name='delete_hospital'),
    path('hospital_info/<str:id>', h_views.hospital_info, name='hospital_info'),
    path('ambulance_req/', am_views.ambulance_req, name='ambulance_req'),
    path('ambulance_req/', am_views.ambulance_req, name='ambulance_req'),
    path('ambulance_req_success/', am_views.ambulance_req_success, name='ambulance_req_success'),
    path('complete_ambulance/<int:id>/', am_views.complete_ambulance_request,name='complete_ambulance_request'),
    path('my_ambulance_requests/', am_views.user_ambulance_requests, name='user_ambulance_requests'),
    path('test_available_list/', dt_views.test_available_list, name='test_available_list'),
    path('upload_test/', dt_views.upload_test, name='upload_test'),
    path('update_test/<str:id>', dt_views.update_test, name='update_test'),
    path('delete_test/<str:id>', dt_views.delete_test, name='delete_test'),


] +static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

