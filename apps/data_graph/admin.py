from django.contrib import admin

# Register your models here.
from apps.data_graph.models import GraphObject, GraphObjectDrawing


class GraphObjectAdmin (admin.ModelAdmin):
    list_display = ('user','name','title','fields','drawing',)
    ordering = ('user','name')
    #list_filter = (
    #    ('ip'),('user'),('event'),
    #)

class GraphObjectDrawingAdmin (admin.ModelAdmin):
    list_display = ('json',)

admin.site.register(GraphObject, GraphObjectAdmin)
admin.site.register(GraphObjectDrawing, GraphObjectDrawingAdmin)
