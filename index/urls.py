"""Shiva_techno URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from index import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('list',views.list,name='list'),
    path('if_else',views.if,name='if_else'),
    path('Dictionary',views.Dictionary,name='Dictionary'),
    path('string',views.string,name='string'),
    path('Loops',views.Loops,name='Loops'),
    path('A_python',views.A_python,name='A_python'),

    path('login',views.loginuser,name='login'),
    path('logout',views.logUser,name='logout'),
    path('signup',views.signup,name='signup'),



# Projects
    path('project_1', views.project_1, name='project1'),
    path('project_2', views.project_2, name='project2'),
    path('project_3', views.project_3, name='project3'),

    path('project_shiva', views.project_shiva, name='project2'),
    path('project_shilpi', views.project_shilpi, name='project2'),
    path('project_rohit', views.project_rohit, name='project2'),


    path('basic_python_a',views.basic_python_a,name='basic_python_a'),

# Blogs 
    path('blogs',views.blogs,name='blogs'),
    path('dash',views.dashboard_b,name='blogs'),
   
    path('addpost',views.addpost,name='blogs'),
    path('updateblog',views.updateblog,name='blogs'),
    path('updatepost/<str:id>',views.update_post,name='updatepost'),
    
  
 
]
