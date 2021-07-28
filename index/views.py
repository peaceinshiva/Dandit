from django.shortcuts import render,redirect,HttpResponseRedirect
from datetime import datetime
from index.models import Contact,b_Post
# Create your views here.
from django.contrib import messages
import smtplib
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout



def home(request):
    # if request.user.is_authenticated:
    #     return render(request,'regist/home_login.html')
    # else:
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')




def project_1(request):
    if request.user.is_authenticated:
        return render(request,'project/project_1.html')
        
    else:
        messages.warning(request, 'First login your account')
        return render(request,'regist/login.html')



def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        query=request.POST.get('query')
        contact=Contact(name=name,email=email,query=query,date=datetime.today())
        contact.save()
        mal=(f"Thank you {name} for your Interest we will Contact you sooon ")
        
        server=smtplib.SMTP_SSL('smtp.gmail.com',465)
        server.login("shivatechnogroup@gmail.com","Shiva@321")

        server.sendmail("shivatechnogroup@gmail.com",email,mal)

        messages.success(request, 'We Got your Query we will contact you soon.')
    return render(request,'contact.html')
    



def logUser(request):
    messages.success(request, 'Logout Succecfull')
    
    messages.success(request, f'Thanks {request.user.get_short_name()} to Using this sites')
    logout(request)
    return render(request,'home.html')
    
def loginuser(request):
    if request.method=='POST':
        email=request.POST.get('email')
        pas=request.POST.get('pass')
        user = authenticate(username=email, password=pas)
        logout(request)
        if user is not None:
            login(request,user)
            messages.success(request, f'Welcome {request.user.get_short_name()} to Shiva Techno Group')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
            # return render(request,'home.html')
        else:
            messages.warning(request, 'Invalid username or password')  
    return render(request,'regist/login.html')

        

       
    


    

def signup(request):
    if request.method=='POST':
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        psw=request.POST.get('psw')
        psw_repeat=request.POST.get('psw_repeat')

        if psw==psw_repeat:
            
            try:
                user = User.objects.create_user(email,email,psw)

                user.first_name =name
                user.last_name  = phone
                
                user.save()
                mal=(f"Thank you {name} to Register Your Account\n Now you can Access all answer ")
                
                
                # server=smtplib.SMTP_SSL('smtp.gmail.com',465)
                # server.login("shivatechnogroup@gmail.com","Asdf@54321")

                # server.sendmail("shivatechnogroup@gmail.com",email,mal)

                messages.success(request, mal)
            except Exception:
                messages.warning(request,"Email Id is  already Exists, Please Try another one !!!")
        else:
            messages.warning(request,"Your Password and Confirm password not matched")
    return render(request,'regist/signup.html')



















# Question python page

def list(request):
    return render(request,'questions/list.html')

def if_(request):
    return render(request,'questions/if.html')
def Loops(request):
    return render(request,'questions/Loops.html')

def Dictionary(request):
    return render(request,'questions/Dictionary.html')

def string(request):
    return render(request,'questions/string.html')

def A_python(request):
    return render(request,'questions/A_python.html')


def python_answer(request):
    if request.user.is_authenticated:
        return render(request,'answer/basic_python_a.html')
    else:
        messages.warning(request, 'First login your account')
        return render(request,'regist/login.html')
        # return render(request,'regist/login.html')
    






# Create  Projects 

def project_1(request):
    if request.user.is_authenticated:
        return render(request,'project/project_1.html')
        
    else:
        messages.warning(request, 'First login your account')
        return render(request,'regist/login.html')
        

def project_2(request):
    if request.user.is_authenticated:
        return render(request,'project/project_2.html')
        
    else:
        messages.warning(request, 'First login your account')
        return render(request,'regist/login.html')


def project_3(request):
    if request.user.is_authenticated:
        return render(request,'project/project_3.html')
        
    else:
        messages.warning(request, 'First login your account')
        return render(request,'regist/login.html')


def project_rohit(request):
    if request.user.is_authenticated:
        return render(request,'project/project_rohit.html')
        
    else:
        messages.warning(request, 'First login your account')
        return render(request,'regist/login.html')

def project_shilpi(request):
    if request.user.is_authenticated:
        return render(request,'project/project_shilpi.html')
        
    else:
        messages.warning(request, 'First login your account')
        return render(request,'regist/login.html')

def project_shiva(request):
    if request.user.is_authenticated:
        return render(request,'project/project_shiva.html')
        
    else:
        messages.warning(request, 'First login your account')
        return render(request,'regist/login.html')



def basic_python_a(request):
    if request.user.is_authenticated:
        return render(request,'answer/basic_python_a.html')
        
    else:
        messages.warning(request, 'First login your account')
        return render(request,'regist/login.html')




# Blogs views

def blogs(request):
    posts=b_Post.objects.all()
    return render(request,'blog/blogs.html',{'posts':posts})

def dashboard_b(request):
    
    if request.user.is_authenticated:
        userna=request.user.get_username()
        # posts=b_Post.objects.all()
        posts=(b_Post.objects.filter(email=userna))
        # print(posts)
        return render(request,'blog/dash.html',{'posts':posts})
    
    else:
        messages.warning(request, 'First login your account')
        return render(request,'regist/login.html')






def addpost(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            autho=request.user.get_short_name()
            userna=request.user.get_username()
            title=request.POST.get('title')
            descr=request.POST.get('query')
            autho=str({request.user.get_short_name()})
            autho=autho[2:-2]
            post=b_Post(author=autho,title=title,description=descr,email=userna)
            post.save()
            messages.success(request, 'We Add your blogs in our Timelines .')
            posts=b_Post.objects.all()
            return render(request,'blog/dash.html',{'posts':posts})
        else:
            
            return render(request,'blog/addpost.html')
        
    else:
        messages.warning(request, 'First login your account')
        return render(request,'regist/login.html')

def updateblog(request):
    if request.method=='POST':
        posts=b_Post.objects.all()
        if request.POST.get('choice')=='Update':
            messages.success(request, 'We Update  your blogs in our Timelines .')
            id=request.POST.get('id')
            title=request.POST.get('title')
            desc=request.POST.get('desc')
            print(id)
            reg = b_Post(id=id,title=title,description=desc)
            reg.save()
        elif request.POST.get('choice')=='Delete':
            messages.success(request, 'Successfully Deleted your blogs')
            reg = b_Post(id=request.POST.get('id'))
            reg.delete()
        else:
            print("else")
            messages.success(request, 'You have not selected options Delete or update')
            id=request.POST.get('id')
            posts=(b_Post.objects.filter(id=id))
            return render(request,'blog/updatepost.html',{'posts':posts})
    return render(request,'blog/dash.html',{'posts':posts})
        
        

def update_post(request,id):
    if request.user.is_authenticated:
        posts=(b_Post.objects.filter(id=id))
        return render(request,'blog/updatepost.html',{'posts':posts})
    else:
        messages.warning(request, 'First login your account')
        return render(request,'regist/login.html')


def deleteblog(request):

    if request.user.is_authenticated:
        messages.warning(request, 'Your Account Deleted')
        posts=b_Post.objects.all()
        return render(request,'blog/dash.html',{'posts':posts})

    else:
        messages.warning(request, 'First login your account')
        return render(request,'regist/login.html')

