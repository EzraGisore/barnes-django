from __future__ import unicode_literals
from django_daraja.mpesa import utils
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django_daraja.mpesa.core import MpesaClient
from decouple import config
from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import User

cl = MpesaClient()
stk_push_callback_url = 'https://api.darajambili.com/express-payment'
b2c_callback_url = 'https://api.darajambili.com/b2c/result'

def oauth_success(request):
    r = cl.access_token()
    return JsonResponse(r, safe=False)


def lipamimi(request):
    if request.method == "POST":
        phone_number = request.POST.get('phone')
        amount = request.POST.get('amount')
        amount = int(amount)
        account_reference = 'BarnesClub'
        transaction_desc = 'STK Push Description'
        callback_url = stk_push_callback_url
        r = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
        return JsonResponse(r.response_description, safe=False)

    return render(request, 'payments.html')


def login(request):
    return render(request,"login.html")
def register(request):
    return render(request,"register.html")
def home(request):
    return render(request,"index (copy).html")
def dash(request):
    return render(request,"Member Dashboard.html")
def register_page(request):
    data = User.objects.all()
    context = {'data': data}
    return render(request, 'login.html', context)

def insertdata(request):
    if request.method == "POST":
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        regID = request.POST.get('regID')
        membership = request.POST.get('membership')
        amount = request.POST.get('amount')

        query = User(name=name, gender=gender,age=age,email=email, phone=phone, regID=regID, membership=membership, amount=amount,)
        query.save()
        return redirect('dash')

    return render(request, 'Member Dashboard.html')


def delete_data(request, id):
    d = User.objects.get(id=id)
    d.delete()
    return redirect('login')
    return render(request, 'login.html')
def updatedata(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        regID = request.POST.get('regID')
        membership = request.POST.get('membership')
        amount = request.POST.get('amount')

        update_info=User.objects.get(id=id)
        update_info.name = name
        update_info.gender = gender
        update_info.age = age
        update_info.email = email
        update_info.phone = phone
        update_info.regID = regID
        update_info.membership = membership
        update_info.amount = amount

        update_info.save()
        return redirect("/")
    d=User.objects.get(id=id)
    context = {"d": d}
    return render(request, 'edit.html', context)