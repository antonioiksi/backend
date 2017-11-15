from apps.data_bin.mixins import ElasticBinItemMixin
from apps.elastic.views.view_drill_search import DrillSearchView


class DataBinDrillSearchView(ElasticBinItemMixin, DrillSearchView):
    """
    Add
    """
