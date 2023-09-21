from django.db import models

# Create your models here.

class news(models.Model):
    title=models.CharField(max_length=30,verbose_name="عنوان خبر")
    txt=models.TextField(verbose_name="متن خبر")
    dtm=models.CharField(max_length=10,default="1402/06/25",verbose_name="تاریخ خبر")
    catgory=models.CharField(max_length=30,default="عمومی",verbose_name="گروه خبری")
    writer=models.CharField(max_length=30,default="مدیرسایت",verbose_name="نویسنده")

    def __str__(self) -> str:
        return self.title
    

