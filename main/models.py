from django.db import models

# Create your models here.
class File(models.Model):
    file= models.FileField(blank=False,null=False)
    file= models.FileField(blank=False,null=False)
    remark=models.CharField(max_length=50)
    timestamp=models.DateField( auto_now_add=True)