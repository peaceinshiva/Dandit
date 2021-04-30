from django.shortcuts import render,HttpResponse
from datetime import datetime
from index.models import Contact
# Create your views here.
from django.contrib import messages
import smtplib


def registration(request):
    
    return render(request,'registration.html')



def home(request):
    
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')


def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        query=request.POST.get('query')
        contact=Contact(name=name,email=email,query=query,date=datetime.today())
        contact.save()
        mal=(f"Thank you {name} for your Interest we will Contact you sooon ")
        
        
        server=smtplib.SMTP_SSL('smtp.gmail.com',465)
        server.login("shivatechnogroup@gmail.com","Asdf@54321")

        server.sendmail("shivatechnogroup@gmail.com",email,mal)

        messages.success(request, 'We Got your Query we will contact you soon.')
    return render(request,'contact.html')


# Question python page

def list(request):
    return render(request,'questions/list.html')

def If_else(request):
    return render(request,'questions/if_else.html')
def Loops(request):
    return render(request,'questions/Loops.html')

def Dictionary(request):
    return render(request,'questions/Dictionary.html')

def string(request):
    return render(request,'questions/string.html')

def A_python(request):
    return render(request,'questions/A_python.html')


