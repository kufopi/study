from django.urls import path
from . import views

urlpatterns = [
    path('camasform/', views.camas, name='camas' ),
    path('conasform/', views.conas, name='conas' ),
]