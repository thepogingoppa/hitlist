from django.shortcuts import render
from . models import People

# Create your views here.
def landing(request):
    return render(request, "hitlist/index.html")

def home(request):
    current_user = request.user
    context = {
        "peoples": People.objects.all(),
        "user": current_user
    }
    return render(request, "hitlist/home.html",context)