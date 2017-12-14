from django.conf.urls import url

from .views import LoadGraphFromBinView, ClearGraphView

urlpatterns = [

    url(r'^load/(?P<bin_pk>.+)/(?P<graph_pk>.+)$', LoadGraphFromBinView.as_view(), name='load'),
    url(r'^clear/$', ClearGraphView.as_view(), name='clear'),

]