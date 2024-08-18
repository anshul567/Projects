from django.shortcuts import render,redirect # type: ignore
from .forms import Contactform

# Create your views here.

def contact_us(request):
    if request.method=='POST':
        form=Contactform(request.POST)
        if form.is_valid():
            form.send_email()
            return redirect('contact_success')
    else:
        context = {'form':Contactform()}
        return render(request,'contact_us/form.html',context)


def contact_success(request):
    return render(request, 'contact_us/success.html')