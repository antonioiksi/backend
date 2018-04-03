from django.contrib import admin

from . import models


# Register your models here.

class MappingTypeAdmin(admin.ModelAdmin):
    list_display = ('title',)
    ordering = ('title',)


class AttributeAdmin(admin.ModelAdmin):
    list_display = ('name', )
    ordering = ('name', )


class EntityAttributeAdmin(admin.ModelAdmin):
    list_display = ('name', 'title',)
    ordering = ('title',)


admin.site.register(models.MappingType, MappingTypeAdmin)
admin.site.register(models.Attribute, AttributeAdmin)
admin.site.register(models.EntityAttribute, EntityAttributeAdmin)
