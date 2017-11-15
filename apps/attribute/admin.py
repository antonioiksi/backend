from django.contrib import admin
from . import models

# Register your models here.

class AttributeAdmin (admin.ModelAdmin):
    list_display = ('name','title')
    ordering = ('name','title')



admin.site.register(models.Attribute, AttributeAdmin)
