from django.contrib.postgres.fields import ArrayField
from django.db import models

from apps.data_graph.comparators import COMPARATOR_CHOICES, EQUAL

# from apps.data_graph.models.GraphAttributeComparator import GraphAttributeComparator


class GraphRelation(models.Model):
    """
    Graph Relation
    """
    graph = models.ForeignKey('data_graph.Graph', on_delete=models.CASCADE, blank=False, null=False, )
    name = models.CharField(u'Name', blank=False, null=False, max_length=100)
    # comparators = ArrayField(GraphAttributeComparator(), blank=False)  # array of fields names

    """
    comparators = models.ManyToManyField('data_graph.GraphAttributeComparator',
                                     related_name='relation_comparators')
    """
    # GraphRelation.objects.relation_comparators.all()

    from_fields = ArrayField(models.CharField(max_length=100), blank=False)  # array of fields names
    to_fields = ArrayField(models.CharField(max_length=100), blank=False)  # array of fields names
    comparators = ArrayField(models.CharField(
        max_length=50,
        choices=COMPARATOR_CHOICES,
        default=EQUAL,
        blank=False, null=False
    ), blank=False, help_text="choose from 'equal, similar, translit_similar', write without whitespaces")

    class Meta:
        verbose_name = 'Graph relation'
        verbose_name_plural = 'Graph relations'

    def __str__(self):
        return self.name
