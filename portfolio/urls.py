from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='portfolio-home'),
    path('about/', views.about, name='portfolio-about'),
    path('services/', views.services, name='portfolio-services'),
    path('contact/', views.contact, name='portfolio-contact')
]