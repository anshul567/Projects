from django.shortcuts import render,redirect # type: ignore
from django.contrib.auth import * # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from django.contrib.auth.mixins import LoginRequiredMixin # type: ignore
from django.view import View # type: ignore
from django.contrib.auth.models import User # type: ignore
from .forms import RegisterForm

# Create your views here.


def register_view(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=User.objects.create_user(username=username, password=password)
            login(request,user)
            return redirect('index')
    else:
        form=RegisterForm()
        return render(request, 'auth/register.html', {'form':form})  
    

def login_view(request):
    pass

def logout_view(request):
    pass



