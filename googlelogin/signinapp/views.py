from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.

def signin(request):
    if not request.user.is_authenticated:
        return render(request,'signin.html')
    else:
         return HttpResponseRedirect('profile/')

    return render(request,'signin.html')

def profile(request):
    if not request.user.is_authenticated:
        if request.method == "POST":    
            return HttpResponseRedirect('profile/')
        else:
            return HttpResponseRedirect('')
        
    else:
        return render(request,'profile.html')
