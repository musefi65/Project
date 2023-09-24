from django.shortcuts import render,HttpResponse
from .models import *
# Create your views here.
def home(request):
    l=news.objects.all()
    return render(request,"newsapp\index.html",context={"news":l})


def shownews(request,adad):
    l=news.objects.get(id=adad)
    return render(request,"newsapp\shownews.html",context={"news":l})

def contact(request):
    n=request.GET.get("nam")
    e=request.GET.get("email")
    t=request.GET.get("tel")
    s=request.GET.get("onvan")
    m=request.GET.get("matn")
    if(n and e and s and m):
        contactcls.objects.create(name=n,email=e,mobile=t,subject=s,message=m)
        return render(request,"newsapp/message.html")
    return render(request,"newsapp/contact.html")

  