from django.contrib.postgres.fields import JSONField, ArrayField
from django.db import models

# Create your models here.
class Graph(models.Model):
    """
    Graph object
    """
    name = models.CharField(u'Name', blank=False, null=False, max_length=100)
    user = models.ForeignKey('auth.User', null=False, blank=False)
    active = models.BooleanField(u'Active', null=False, blank=False, default=False)

    class Meta:
        verbose_name = 'Graph'
        verbose_name_plural = 'Graph list'

    def __str__(self):
        return self.name


class GraphModel(models.Model):
    """
    Graph Model
    """
    graph = models.ForeignKey('data_graph.Graph', on_delete=models.CASCADE, blank=False, null=False,)
    name = models.CharField(u'Name', blank=False, null=False, max_length=100)
    fields = ArrayField(models.CharField(max_length=100), blank=False)  # array of fields names
    drawing = models.ForeignKey('data_graph.GraphModelDrawing', blank=True, null=True, default=None)

    class Meta:
        verbose_name = 'Graph model'
        verbose_name_plural = 'Graph models'

    def __str__(self):
        return self.name

class GraphModelDrawing(models.Model):
    """
    Graph Model Drawing
    """
    name = models.CharField(u'Name', blank=False, null=False, max_length=100)
    json = JSONField(blank=False, null=True, verbose_name="json")

    class Meta:
        verbose_name = 'Graph model drawing'
        verbose_name_plural = 'Graph model drawings'

    def __str__(self):
        return self.name


class GraphRelation(models.Model):
    """
    Graph Relation
    """
    graph = models.ForeignKey('data_graph.Graph', on_delete=models.CASCADE, blank=False, null=False,)
    name = models.CharField(u'Name', blank=False, null=False, max_length=100)
    from_fields = ArrayField(models.CharField(max_length=100), blank=False)  # array of fields names
    to_fields = ArrayField(models.CharField(max_length=100), blank=False)  # array of fields names

    class Meta:
        verbose_name = 'Graph relation'
        verbose_name_plural = 'Graph relations'

    def __str__(self):
        return self.name
