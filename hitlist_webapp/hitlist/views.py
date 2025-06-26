from django.shortcuts import render
from . models import People

# Create your views here.
def landing(request):
    return render(request, "hitlist/index.html")

def home(request):
    context = {
        "peoples": People.objects.all()
    }
    return render(request, "hitlist/home.html",context)