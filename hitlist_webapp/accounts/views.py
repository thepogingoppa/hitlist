from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('hitlist-home')
    else:
        form = UserCreationForm()
    
    return render(request, "accounts/signup.html", {'form': form })

# def register(request):
#     form = UserCreationForm()
#     return render(request, 'accounts/signup.html', {'form': form})