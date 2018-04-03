from apps.csv.views import CsvLoadView
from apps.data_bin.mixins import BinItemDataEnrichFirstLevelMixin
from apps.elastic.views.view_drill_search import DrillSearchView
from apps.elastic.views.view_mapped_search import MappedSearchView
from apps.elastic.views.view_simple_search import SimpleSearchView


class ElasticView(BinItemDataEnrichFirstLevelMixin, DrillSearchView):
    """
    DataBinDrillSearchView
    """


class CsvView(BinItemDataEnrichFirstLevelMixin, CsvLoadView):
    """
    DataBinDrillSearchView
    """


class DataBinSimpleSearchView(BinItemDataEnrichFirstLevelMixin, SimpleSearchView):
    """
    Add
    """


class DataBinMappedSearchView(BinItemDataEnrichFirstLevelMixin, MappedSearchView):
    """
    Add
    """
