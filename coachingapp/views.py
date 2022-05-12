from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.contrib import auth

from django.http import HttpResponseRedirect
# Create your views here.





def home(reqest):
    return render(reqest,'home.html')

def gallery(reqest):
    return render(reqest,'gallery.html')  

def about(reqest):
    return render(reqest,'about.html')  

def contact(reqest):
    return render(reqest,'contact.html') 

def courses(reqest):
    return render(reqest,'courses.html')  

def moreca(reqest):
    return render(reqest,'moreca.html') 

def registerca(reqest):
    return render(reqest,'registerca.html') 

def morecma(reqest):
    return render(reqest,'morecma.html')  

def moresap(reqest):
    return render(reqest,'moresap.html')  

def loginpage(request):
    return render(request,'login.html')
def signup(request):
    return render(request,'signup.html')
def usercreate(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        email=request.POST['email']

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'This usernae already exists!!!')
                print("Username already taken..")
                return redirect('signup')
            else:
                user=User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username= username,
                    password= password,
                    email= email)
                user.save()
                print("successed")
                return redirect('loginpage')
        else:
            messages.info(request,'Password doesnt match!!!!')
            print("password is not matching...")
            return redirect('signup')
    
    else:
        return render(request,'signup.html')
#login
def userlogin(request):
   if request.method == 'POST':
       username=request.POST['username']
       password=request.POST['password']
       user=auth.authenticate(username=username,password=password)
       if user is not None:
           auth.login(request,user)
           messages.info(request, f'Welcome {username}')
           return redirect('about')
       else:
           messages.info(request,'Invalid Username or Password.Try Again.')
           return redirect('loginpage')
   else:
       return redirect('loginpage')
#logout
@login_required(login_url='userlogin')
def userlogout(request):
   auth.logout(request)
   return redirect('home')