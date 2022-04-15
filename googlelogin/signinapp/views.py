from turtle import title
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from .models import blog, history

from .models import blog
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
        bg = blog.objects.all()
        return render(request,'profile.html',{'blog':bg})

def search(request):
    if 'term' in request.GET:
        qs= blog.objects.filter(title__icontains=request.GET.get('term')) #| blog.objects.filter(desc__icontains=request.GET.get('term'))
        title = list()
        for b in qs:
            title.append(b.title)
        return JsonResponse(title,safe=False)
    query = request.GET.get('query')
    
    res = history.objects.filter(user=request.user, search_content= query).exists()
    
    if res == False:
        his = history(user=request.user,search_content=query)
        his.save()

    bg = []
    if query:
        bg = blog.objects.filter(title__icontains=query) | blog.objects.filter(desc__icontains=query)
        print(bg)
        
    data = history.objects.filter(user = request.user).order_by('-id')
    print(data)
    return render(request,'search.html',{'blog':bg,'data':data})