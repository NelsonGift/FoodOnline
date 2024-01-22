from django.urls import path
from .import views

urlpatterns=[
    path('registeruser/', views.registerUser, name='registerUser'),
    path('registerVendor/', views.registerVendor, name='registerVendor'),

]