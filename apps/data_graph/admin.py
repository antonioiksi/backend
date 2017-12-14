from django.contrib import admin

# Register your models here.
from apps.data_graph.models.model_graph import Graph, GraphModel, GraphRelation, GraphModelDrawing
from apps.data_graph.models.model_graph_data import GraphData, GraphNode


class GraphAdmin (admin.ModelAdmin):
    list_display = ('name', 'user', 'active' )
    ordering = ('user','name')
    list_filter = (
        ('user'),
    )


class GraphModelAdmin (admin.ModelAdmin):
    list_display = ('graph', 'name', 'fields', 'drawing',)
    ordering = ('graph', 'name')
    #list_filter = (
    #    ('ip'),('user'),('event'),
    #)


class GraphRelationAdmin (admin.ModelAdmin):
    list_display = ('graph', 'name', 'from_fields', 'to_fields',)
    ordering = ('graph', 'name')


class GraphModelDrawingAdmin (admin.ModelAdmin):
    list_display = ('name', 'json',)


class GraphDataAdmin (admin.ModelAdmin):
    list_display = ('graph', 'data', )

class GraphNodeAdmin (admin.ModelAdmin):
    list_display = ('pk', 'graph', 'model', 'graph_data', )
    ordering = ('pk',)


admin.site.register(Graph, GraphAdmin)
admin.site.register(GraphModel, GraphModelAdmin)
admin.site.register(GraphRelation, GraphRelationAdmin)
admin.site.register(GraphModelDrawing, GraphModelDrawingAdmin)

admin.site.register(GraphData, GraphDataAdmin)
admin.site.register(GraphNode, GraphNodeAdmin)
