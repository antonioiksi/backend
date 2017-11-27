from apps.data_bin.mixins import ElasticBinItemMixin
from apps.elastic.views.view_drill_search import DrillSearchView
from apps.elastic.views.view_mapped_search import MappedSearchView
from apps.elastic.views.view_simple_search import SimpleSearchView


class DataBinDrillSearchView(ElasticBinItemMixin, DrillSearchView):
    """
    Add
    """


class DataBinSimpleSearchView(ElasticBinItemMixin, SimpleSearchView):
    """
    Add
    """


class DataBinMappedSearchView(ElasticBinItemMixin, MappedSearchView):
    """
    Add
    """
