from django.shortcuts import render,HttpResponse
from .models import *
# Create your views here.
def home(request):
    l=news.objects.all()
    return render(request,"newsapp\index.html",context={"news":l})


def shownews(request,adad):
    l=news.objects.get(id=adad)
    return render(request,"newsapp\shownews.html",context={"news":l})

def contactus(request):
    l=news.objects.all()
    return render(request,"newsapp\contact.html",context={"news":l})
