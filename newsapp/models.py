from django.db import models

# Create your models here.

class site_setting(models.Model):
    NAM=models.CharField(max_length=24,verbose_name="نام وبسایت")

class news(models.Model):
    title=models.CharField(max_length=30,verbose_name="عنوان خبر")

    titr1=models.TextField(verbose_name="تیتر یـک ",default=" تیتر ")
    titr2=models.TextField(verbose_name=" تیتر دو ",default=" تیتر ")
    titr3=models.TextField(verbose_name="تیتر سـه ",default=" تیتر ")

    txt1=models.TextField(verbose_name="متن یک خبر",default="خبر")
    txt2=models.TextField(verbose_name="متن دو خبر",default=" متن خبر")
    txt3=models.TextField(verbose_name="متن سه خبر",default=" متن خبر")
    txt4=models.TextField(verbose_name="متن چهار خبر",default=" متن خبر")
    txt5=models.TextField(verbose_name="متن پنج خبر",default=" متن خبر")
    txt6=models.TextField(verbose_name="متن شش خبر",default=" متن خبر")
    txt7=models.TextField(verbose_name="متن هفت خبر",default=" متن خبر")

    
    pic1=models.ImageField(upload_to="pictures",verbose_name="عکس دو")
    pic2=models.TextField(verbose_name="عکس دو",default=" عکس خبر")
    pic3=models.TextField(verbose_name="عکس سه",default=" عکس خبر")
    pic4=models.TextField(verbose_name="عکس چهار",default=" عکس خبر")
    pic5=models.TextField(verbose_name="عکس پنج",default=" عکس خبر")

    
    
    dtm=models.CharField(max_length=10,default="1402/06/25",verbose_name="تاریخ خبر")
    catgory=models.CharField(max_length=30,default="عمومی",verbose_name="گروه خبری")
    writer=models.CharField(max_length=30,default="مدیرسایت",verbose_name="نویسنده")


    keyword1=models.CharField(max_length=60,default="هفته نامه امین بختیاری ",verbose_name="کلمات کلیدی")
    keyword2=models.CharField(max_length=60,default="هفته نامه امین بختیاری ",verbose_name="کلمات کلیدی")
    keyword3=models.CharField(max_length=60,default="هفته نامه امین بختیاری ",verbose_name="کلمات کلیدی")
    keyword4=models.CharField(max_length=60,default="هفته نامه امین بختیاری ",verbose_name="کلمات کلیدی")

    def __str__(self) -> str:
        return self.title
    

 
class contact_us(models.Model):
    name=models.CharField(max_length=40,) 
    email=models.CharField(max_length=50,)
    mobile=models.CharField(max_length=50)
    subject=models.CharField(max_length=200)
    message=models.CharField(max_length=500)  

    def __str__(self) :
        return self.subject
    

class coment(models.Model):
    newss=models.ForeignKey(news,on_delete=models.CASCADE)
    sender=models.CharField(max_length=50)
    comentxt=models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.sender

    