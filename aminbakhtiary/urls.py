
from django.contrib import admin
from django.urls import path
from newsapp.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    #برای ساختن نمایش خبر 
    path('news/<int:adad>', shownews),
    path('contact', contact), 
    path('aboutus', home),

]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)