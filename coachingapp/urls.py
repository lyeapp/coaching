from django.urls import path
from coachingapp import views
from django.shortcuts import render

urlpatterns = [
    path('',views.home,name='home'),
    path('gallery',views.gallery,name='gallery'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('courses',views.courses,name='courses'),
    path('moreca/',views.moreca,name='moreca'),
    path('registerca',views.registerca,name='registerca'),
    path('morecma/',views.morecma,name='morecma'),
    path('moresap/',views.moresap,name='moresap'),
    path('signup',views.signup,name='signup'),
    path('usercreate',views.usercreate,name='usercreate'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('userlogin',views.userlogin,name='userlogin'),
    # path('logout',views.logout,name='logout'),
    # path('user_home',views.userhome,name='user_home'),
    # path('admin_home',views.adminhome,name='admin_home'),
    path('userlogout',views.userlogout,name='userlogout'),
    
    ]