from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name="index"),
    path('about', views.about, name="about"),
    path('resume', views.resume, name="resume"),
    path('service', views.service, name="service"),
    path('contact', views.contact, name="contact"),
]
