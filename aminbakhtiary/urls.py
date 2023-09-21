
from django.contrib import admin
from django.urls import path
from newsapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    #برای ساختن نمایش خبر 
    path('news/<int:adad>', shownews), 


]
