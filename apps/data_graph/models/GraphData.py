import json

from django.contrib.postgres.fields import JSONField
from django.db import models


class GraphData(models.Model):
    """
    Flat data for graph building
    """
    graph = models.ForeignKey('data_graph.Graph', on_delete=models.CASCADE, blank=False, null=False, )
    data = JSONField(blank=True, null=True, verbose_name="data")

    class Meta:
        verbose_name = 'Graph data row'
        verbose_name_plural = 'Graph data'

    def __str__(self):
        return json.dumps(self.data)
