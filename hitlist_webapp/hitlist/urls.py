from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.home, name='hitlist-home'),
    
    path('', views.landing, name='hitlist-landing')
]