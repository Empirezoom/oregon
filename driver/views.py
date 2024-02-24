from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
from django.contrib import messages 
from . forms import *

from django.shortcuts import get_object_or_404
# Create your views here.


def homepage(request):

    apply = ApplicationChoice.objects.all()

    contact = ContactForm()
    if request.method == 'POST':
        contact = ContactForm(request.POST)
        if contact.is_valid():
            contact.save()
            messages.success(request,'Your message has been sent successfully!')
            return redirect('message')


    context = {
        'apply':apply,
        'contact':contact,
    }
    
    return render(request,'index.html',context)


def application(request,id,slug):
    
    applicant = ApplicationChoice.objects.get(pk=id)
    apply = ApplicationForm()
    if request.method == 'POST':
        apply = ApplicationForm(request.POST)
        if apply.is_valid():
            apply.save()
            messages.success(request,'successful!')
            return redirect('payment',id=id,slug=slug)


    context = {
        'applicant':applicant,
        'apply':apply,
    }

    return render(request,'details.html',context)


def payment(request,id,slug):
    
    applicant = ApplicationChoice.objects.get(pk=id)

    btc = BtcInfo.objects.get(pk=1)
    bnb = BnbInfo.objects.get(pk=1)
    doge = DogeInfo.objects.get(pk=1)



    context = {
        'applicant':applicant,
        'btc':btc,
        'bnb':bnb,
        'doge':doge,
      
    }

    return render(request,'payment.html',context)


def confirmation(request,id,slug):
    
    applicant = ApplicationChoice.objects.get(pk=id)

    if request.method == 'POST':
        upload = UploadForm(request.POST,request.FILES)
        if upload.is_valid():
            upload.save()
            messages.success(request,'updated!')
            return redirect('thanks',id=id,slug=slug)
        else:
            upload = UploadForm()


    context = {
        'applicant':applicant,
      
    }

    return render(request,'confirmation.html',context)


def thanks(request,id,slug):
    
    applicant = ApplicationChoice.objects.get(pk=id)

    thanks_edit = ThanksEdit.objects.get(pk=1)


    context = {
        'applicant':applicant,
        'thanks_edit':thanks_edit,
      
    }

    return render(request,'received.html',context)

def message(request):
    
 



    return render(request,'message.html')


