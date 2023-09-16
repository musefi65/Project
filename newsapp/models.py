from django.db import models

# Create your models here.

class news(models.Model):
    title=models.CharField(max_length=30)
    txt=models.TextField()
    dtm=models.CharField(max_length=10,default="1402/06/25")
    catgory=models.CharField(max_length=30,default="عمومی")

    def __str__(self) -> str:
        return self.title
    

