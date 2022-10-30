from django.contrib import admin
from .models import RewardPoints, Log

# Register your models here.

class info(admin.ModelAdmin):
    list_display = ('name', 'value')
    
admin.site.register(RewardPoints, info)
admin.site.register(Log)