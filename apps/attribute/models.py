from django.db import models

# Create your models here.

class Attribute(models.Model):
    name = models.CharField(u'Name', unique=True, null=False, blank=False,max_length=100)
    title = models.CharField(u'Title', unique=True, null=False, blank=False, max_length=100)

    def __str__(self):
        return "Name %s: Title %s" % (self.name, self.title)


    class Meta:
        verbose_name = 'attribute'
        verbose_name_plural = 'attributes'
