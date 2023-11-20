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
from .models import BcMember
from django.contrib.auth import get_user_model
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .token import account_activation_token
from django.core.mail import EmailMessage

cl = MpesaClient()
stk_push_callback_url = 'https://api.darajambili.com/express-payment'
b2c_callback_url = 'https://api.darajambili.com/b2c/result'

def oauth_success(request):
    r = cl.access_token()
    return JsonResponse(r, safe=False)


def pay(request):
    if request.method == "POST":
        phone_number = request.POST.get('phone')
        amount = 1
        amount = int(amount)
        account_reference = 'Barnes'
        transaction_desc = 'STK Push Description'
        callback_url = stk_push_callback_url
        r = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
        return JsonResponse(r.response_description, safe=False)

    return render(request, 'payments.html')


def login(request):
    return render(request,"login.html")
def register(request):
    return render(request,"register.html")
def about(request):
    return render(request,"about.html")
def project(request):
    return render(request,"project.html")
def staff(request):
    return render(request,"staff.html")
def contact(request):
    return render(request,"contact.html")
def home(request):
    return render(request,"index (copy).html")
def dash(request):
    return render(request,"Member Dashboard.html")
def dashb(request):
    return render(request,"dash.html")
def bc(request):
    return render(request,"bookclub.html")
def register_page(request):
    data = User.objects.all()
    context = {'data': data}
    return render(request, 'login.html', context)

##def insertdata(request):
##    if request.method == "POST":
##        name = request.POST.get('name')
##        gender = request.POST.get('gender')
##        age = request.POST.get('age')
##        email = request.POST.get('email')
##        phone = request.POST.get('phone')
##        regID = request.POST.get('regID')
##        membership = request.POST.get('membership')
##        amount = request.POST.get('amount')

##        query = User(name=name, gender=gender,age=age,email=email, phone=phone, regID=regID, membership=membership, amount=amount,)
##        query.save()
##        return redirect('dash')

##    return render(request, 'Member Dashboard.html')


##def delete_data(request, id):
##    d = User.objects.get(id=id)
##    d.delete()
##    return redirect('login')
##    return render(request, 'login.html')
##def updatedata(request, id):
##    if request.method == "POST":
##        name = request.POST.get('name')
##        gender = request.POST.get('gender')
##        age = request.POST.get('age')
##        email = request.POST.get('email')
##        phone = request.POST.get('phone')
##        regID = request.POST.get('regID')
##        membership = request.POST.get('membership')
##        amount = request.POST.get('amount')

##        update_info=User.objects.get(id=id)
##        update_info.name = name
##        update_info.gender = gender
##        update_info.age = age
##        update_info.email = email
##        update_info.phone = phone
    ##        update_info.regID = regID
    ##   update_info.membership = membership
    ##  update_info.amount = amount

    ##  update_info.save()
    ##  return redirect("/")
    ##d=User.objects.get(id=id)
    ##context = {"d": d}
    ##return render(request, 'edit.html', context)
def memberpay(request):
    return render(request,"MembershipPay.html")
def bcschedule(request):
    return render(request,"bcschedule.html")
def junior(request):
    return render(request,"junior.html")
def jrschedule(request):
    return render(request,"jrschedule.html")
def awards(request):
    return render(request,"awards.html")
def library(request):
    return render(request,"library.html")
def signin(request):
    return render(request,"signin.html")
def insertbcdata(request):
    if request.method == "POST":
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        email = request.POST.get('email')
        phone = request.POST.get('phone')


        query = BcMember(name=name, gender=gender,age=age,email=email, phone=phone,)
        query.save()
        return redirect('bc')

    return render(request, 'bookclub.html')
def delete_bcdata(request, id):
    d = BcMember.objects.get(id=id)
    d.delete()
    return redirect('login')
    return render(request, '/')
def update_bcdata(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        email = request.POST.get('email')
        phone = request.POST.get('phone')


        update_info=BcMember.objects.get(id=id)
        update_info.name = name
        update_info.gender = gender
        update_info.age = age
        update_info.email = email
        update_info.phone = phone


        update_info.save()
        return redirect("/")
    d=BcMember.objects.get(id=id)
    context = {"d": d}
    return render(request, 'edit.html', context)
def insertjrdata(request):
    if request.method == "POST":
        parent_name = request.POST.get('parent_name')
        junior_name = request.POST.get('junior_name')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        parent_email = request.POST.get('parent_email')
        parent_phone = request.POST.get('parent_phone')


        query = JrMember(parent_name=parent_name, junior_name= junior_name, gender=gender,age=age,parent_email=parent_email, parent_phone=parent_phone,)
        query.save()
        return redirect('junior')

    return render(request, 'junior.html')
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # save form in the memory not in database
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            # to get the domain of the current site
            current_site = get_current_site(request)
            mail_subject = 'Activation link has been sent to your email id'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})
def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        ##return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
        return render(request, "MembershipPay.html")
    else:
        return HttpResponse('Activation link is invalid!')