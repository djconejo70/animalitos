from django.contrib import admin
from django.urls import path, include 
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('contacto.html', contacto, name='contacto'),
    path('soporte.html', soporte, name='soporte'),
    
   ]