from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import os

def getFieldName(request,filename):
    now_time = datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename = "%s%s"%(now_time,filename)
    return os.path.join('upload/',new_filename)

class Catagory(models.Model):
    name = models.CharField(max_length=150,null=False,blank=False)
    image = models.ImageField(upload_to=getFieldName,null=True,blank=True)
    description = models.TextField(max_length=500,null=False,blank=False)
    status = models.BooleanField(default=False,help_text="0-show,1-Hidden")
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    catagory = models.ForeignKey(Catagory,on_delete=models.CASCADE)
    name = models.CharField(max_length=150,null=False,blank=False)
    vendor = models.CharField(max_length=150,null=False,blank=False)
    product_image = models.ImageField(upload_to=getFieldName,null=True,blank=True)
    quantity = models.IntegerField(null=False,blank=False)
    original_price = models.FloatField(null=False,blank=False)
    selling_price = models.FloatField(null=False,blank=False)
    description = models.TextField(max_length=500,null=False,blank=False)
    status = models.BooleanField(default=False,help_text="0-show,1-Hidden")
    trending = models.BooleanField(default=False,help_text="0-default,1-Tending")
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self) -> str:
        return self.name
    
class LabourAttendance(models.Model):
    SUBCONTRACTOR = 'F&F'
    MUSTER_ROLE = 'MR'
    EMPTY = ''

    ATTENDANCE_TYPE_CHOICES = [
        (EMPTY, ''),
        (SUBCONTRACTOR, 'Subcontractor'),
        (MUSTER_ROLE, 'Muster Role'),
    ]

    name = models.CharField(max_length=150, null=False, blank=False)
    attendance_type = models.CharField(
        max_length=3,
        choices=ATTENDANCE_TYPE_CHOICES,
        default=EMPTY,
    )
    posting_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    product_qty = models.IntegerField(null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add = True)



