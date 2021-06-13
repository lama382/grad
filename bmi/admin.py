from django.contrib import admin
from bmi import models
# Register your models here.
class BmiAdmin(admin.ModelAdmin):
    list_display=('user','bmi','date')



admin.site.register(models.Bmi, BmiAdmin)    
