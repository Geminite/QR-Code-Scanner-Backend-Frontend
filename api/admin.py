from django.contrib import admin
from .models import RewardPoints, Log, Allocation

# Register your models here.

class info(admin.ModelAdmin):
    list_display = ('name', 'value')

class search(admin.ModelAdmin):
    search_fields = ['source', 'source__icontains', 'date', 'date__icontains']
    list_display = ('source', 'date')
    
admin.site.register(RewardPoints, info)
admin.site.register(Log, search)
admin.site.register(Allocation)