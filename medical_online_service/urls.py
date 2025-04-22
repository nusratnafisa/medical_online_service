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
    path('login/', a_views.login, name='login'),
    path('register/', a_views.register, name='register'),
    path('', d_views.home, name='home'),
    path('doc_search/', d_views.doc_search, name='doc_search'),
    path('doctor_list/', d_views.doctor_list, name='doctor_list'),
    path('book_appointment/', ap_views.book_appointment, name='book_appointment'),
    path('hospital_info/', h_views.hospital_info, name='hospital_info'),
    path('hospital_list/', h_views.hospital_list, name='hospital_list'),
    path('ambulance_req/', am_views.ambulance_req, name='ambulance_req'),
    path('test_available_list/', dt_views.test_available_list, name='test_available_list'),
    path('test_search/', dt_views.test_search, name='test_search'),


]
