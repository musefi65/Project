from django.shortcuts import render,HttpResponse
from .models import *
# Create your views here.
def home(request):
    l=news.objects.all()
    return render(request,"newsapp\index.html",context={"news":l})