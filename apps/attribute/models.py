from django.contrib.postgres.fields import ArrayField
from django.db import models


class Attribute(models.Model):
    """
    This is search system layer.

    we do search through this attributes,
    for example: ElasticSearch has index field 'person_name'
    that means we are able to add attribute 'person_name' and
    do search by this field

    """
    name = models.CharField(u'Name', unique=True, null=False, blank=False, max_length=100)
    title = models.CharField(u'Title', unique=True, null=False, blank=False, max_length=100)

    def __str__(self):
        return "Name: %s, Title: %s" % (self.name, self.title)

    class Meta:
        verbose_name = 'Attribute'
        verbose_name_plural = 'Attributes'
        ordering = ('title',)


class EntityAttribute(models.Model):
    """
    This is business layer

    For example 'phone', 'address'...
    Important not 'person_phone' or 'company_phone'
    The number of entity attributes must be not much,
    the smaller is the better

    """
    name = models.CharField(u'Name', unique=True, null=False, blank=False, max_length=100)
    title = models.CharField(u'Title', unique=True, null=False, blank=False, max_length=100)
    # attributes = ArrayField(models.CharField(max_length=100))
    attributes = models.ManyToManyField(Attribute)

    def __str__(self):
        return "Entity attribute %s" % self.title

    class Meta:
        verbose_name = 'Entity attribute'
        verbose_name_plural = 'Entity attributes'
        ordering = ('title',)
