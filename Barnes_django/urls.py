"""Barnes_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
##    path('delete/<id>', views.delete_data, name= 'deletedata'),
  ##  path('update/<id>', views.updatedata, name='updatedata'),
    path('login/', views.register_page, name='login'),
##    path('insert', views.insertdata, name='insert'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
##    path('', views.insertdata, name='enter'),
    path('pay/', views.pay, name='pay'),
    path('dash/', views.dash, name='dash'),
    path('memberpay/', views.memberpay, name='memberpay'),
    path('about/', views.about, name='about'),
    path('project/', views.project, name='project'),
    path('staff/', views.staff, name='staff'),
    path('contact/', views.contact, name='contact'),
    path('dashb/', views.dashb, name='dashb'),
    path('bookclub/', views.bc, name='bc'),
    path('deletebc/<id>', views.delete_bcdata, name= 'deletebcdata'),
    path('updatebc/<id>', views.update_bcdata, name='updatebcdata'),
    path('insertbc', views.insertbcdata, name='insertbcdata'),
    path('bcschedule/', views.bcschedule, name='bcschedule'),

]
