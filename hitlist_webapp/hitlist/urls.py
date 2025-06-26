from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='hitlist-landing'),
    path('home/', views.home, name='hitlist-home'),
]
