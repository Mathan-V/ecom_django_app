from django.contrib import admin
from .models import *

'''class CatagoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'description' )'''

admin.site.register(Catagory)
admin.site.register(Product)
admin.site.register(LabourAttendance)
# Register your models here.
