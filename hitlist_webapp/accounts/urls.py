from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup/', views.register, name='hitlist-signup'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='hitlist-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='hitlist-logout'),
]
