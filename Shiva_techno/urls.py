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
from django.urls import path,include



admin.site.site_header = "Shiva Techno Group"
admin.site.site_title = "Shiva"
admin.site.index_title = "Welcome to Shiva Techno Group"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('index.urls')),
    path('registration',include('index.urls')),
    path('home',include('index.urls')),
    path('about',include('index.urls')),
    path('contact',include('index.urls')),
    path('list',include('index.urls')),

    path('if_else',include('index.urls')),
    path('string',include('index.urls')),
    path('Loops',include('index.urls')),
    path('Dictionary',include('index.urls')),
    path('A_python',include('index.urls')),


    path('logout',include('index.urls')),
    path('login',include('index.urls')),
    
    path('signup',include('index.urls')),
    path('project_1',include('index.urls')),
    path('project_2',include('index.urls')),
    path('project_3',include('index.urls')),
    path('project_rohit',include('index.urls')),
    path('project_shiva',include('index.urls')),
    path('project_shilpi',include('index.urls')),
    
    path('basic_python_a',include('index.urls')),

    
]
