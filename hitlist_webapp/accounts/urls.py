from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup/', views.register, name='hitlist-signup'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='hitlist-login')
]
