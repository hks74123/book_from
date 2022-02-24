
from django.contrib import admin
from django.urls import path,include
from . import views
  
urlpatterns = [
    path('',views.home),
    path('dsgn/',views.docsign),
    path('psgn/',views.patsign),
    path('register/<slug:pid>/',views.register),
    path('login/<slug:pid>/',views.login),
    path('logout/',views.logout),
    path('booking_form/<slug:pid>/',views.booking_form),
    path('Book_appointment/<slug:pid>/',views.Book_appointment),
]
