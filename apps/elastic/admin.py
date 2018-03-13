from django.contrib import admin

# Register your models here.


from .models import QueryTemplate


class QueryTemplateAdmin (admin.ModelAdmin):
    list_display = ('user','name','title','template')
    #ordering = ('-datetime','user')
    list_filter = (
        ('user'),
    )


admin.site.register(QueryTemplate, QueryTemplateAdmin)