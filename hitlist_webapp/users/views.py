from django.shortcuts import render, redirect
from django.contrib import messages
from . forms import UserRegistrationForm
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('first_name')
            messages.success(request, f'Welcome to your hitlist, {name}!')
            return redirect('hitlist-home')
    else:
        form = UserRegistrationForm() 
    return render(request, 'users/register.html', {'form': form})