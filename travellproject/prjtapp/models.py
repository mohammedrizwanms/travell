from django.db import models

# Create your models here.
class prjttable(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()



class team(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    info=models.TextField()