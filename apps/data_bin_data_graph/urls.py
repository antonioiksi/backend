from django.conf.urls import url

from .views import (ClearGraphView, LoadExtendGraphFromBinView,
                    LoadGraphFromBinView)

urlpatterns = [

    url(r'^load/(?P<bin_pk>.+)/(?P<graph_pk>.+)$', LoadGraphFromBinView.as_view(), name='load'),
    url(r'^load-extend/(?P<bin_pk>.+)/(?P<graph_pk>.+)$', LoadExtendGraphFromBinView.as_view(), name='load'),
    url(r'^clear/$', ClearGraphView.as_view(), name='clear'),

]
