import json

from django.contrib.postgres.fields import JSONField
from django.db import models

class GraphData(models.Model):
    """
    Flat data for graph building
    """
    graph = models.ForeignKey('data_graph.Graph', on_delete=models.CASCADE, blank=False, null=False,)
    data = JSONField(blank=True, null=True, verbose_name="JSON graph data")

    def __str__(self):
        return json.dumps(self.data)


class GraphNode(models.Model):
    """
    """
    graph = models.ForeignKey('data_graph.Graph', on_delete=models.CASCADE, blank=False, null=False,)
    model = models.ForeignKey('data_graph.GraphModel', on_delete=models.CASCADE, blank=False, null=False)
    graph_data = models.ForeignKey('data_graph.GraphData', on_delete=models.CASCADE, blank=False, null=False)


class GraphNodeEdge(models.Model):
    """
    """
    class Meta:
        # делает уникальным направление обмена
        unique_together = ("from_node", "to_node")

    relation = models.ForeignKey('data_graph.GraphRelation', on_delete=models.CASCADE, blank=False, null=False)
    from_node = models.ForeignKey('data_graph.GraphNode', on_delete=models.CASCADE, blank=False, null=False, related_name="from_node")
    to_node = models.ForeignKey('data_graph.GraphNode', on_delete=models.CASCADE, blank=False, null=False, related_name="to_node")
