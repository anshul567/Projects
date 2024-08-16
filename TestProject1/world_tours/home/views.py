from django.shortcuts import render # type: ignore
from .models import Tour

# Create your views here.


def index(request):
    tours=Tour.objects.all()
    context = {'tours':tours}
    return render(request, 'index.html', context)
