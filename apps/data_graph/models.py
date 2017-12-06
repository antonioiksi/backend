from django.contrib.postgres.fields import JSONField, ArrayField
from django.db import models

# Create your models here.
class GraphData(models.Model):
    """
    JSON graph data Model
    """
    user = models.ForeignKey('auth.User',null=True, blank=True, default=None)
    data = JSONField(blank=True, null=True, verbose_name="JSON graph data")


class GraphObject(models.Model):
    """
    JSON graph data Model
    """
    user = models.ForeignKey('auth.User',null=True, blank=True, default=None)   # every user has own graph objects
    name = models.CharField(u'Name', blank=False, null=False, max_length=100)
    title = models.CharField(u'Title', blank=False, null=False, max_length=100)
    fields = ArrayField(models.CharField(max_length=200), blank=False)  # array of fields names
