from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from Home.forms import RegistrationForms

def register(request):
    form = RegistrationForms()
    if request.method == 'POST':
        form = RegistrationForms(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/Home/')
    return render(request,'register.html', {'form':form}) 