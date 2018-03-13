from django.contrib import admin
from . import models


# Register your models here.

class AttributeAdmin(admin.ModelAdmin):
    list_display = ('name', 'title')
    ordering = ('name', 'title')


class EntityAttributeAdmin(admin.ModelAdmin):
    list_display = ('name', 'title',)
    ordering = ('title',)


admin.site.register(models.Attribute, AttributeAdmin)
admin.site.register(models.EntityAttribute, EntityAttributeAdmin)
