from django.shortcuts import render
from . models import Note

# Create your views here.
def home(request):
    context = {
        'Notes': Note.objects.all()
    }
    return render(request, 'hitlist/index.html', context)