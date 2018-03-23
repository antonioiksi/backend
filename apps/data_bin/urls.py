from django.conf.urls import url

from apps.data_bin.views.FlatDataBinView import FlatDataBinView
from apps.data_bin.views.FlatExtendEntityAttributeDataBinView import \
    FlatExtendEntityAttributeDataBinView
from apps.data_bin.views.view_bin import (ActiveBinRetrieveView,
                                          BinActivateView, BinCreateView,
                                          BinDeleteView, BinListView,
                                          BinResetView)
from apps.data_bin.views.view_bin_item import (BinItemDeleteView,
                                               BinItemListView, BinItemView)

urlpatterns = [


    url(r'^activate/(?P<name>.+)$', BinActivateView.as_view(), name='activate'),
    url(r'^get-active/$', ActiveBinRetrieveView.as_view(), name='get-active'),


    url(r'^list/$', BinListView.as_view(), name='list'),
    url(r'^flat-data/(?P<pk>.+)$', FlatDataBinView.as_view(), name='flat-data'),
    url(r'^flat-extend-data/(?P<pk>.+)$', FlatExtendEntityAttributeDataBinView.as_view(), name='flat-extend-data'),

    url(r'^create/$', BinCreateView.as_view(), name='create'),
    url(r'^delete/(?P<pk>.+)$', BinDeleteView.as_view(), name='delete'),

    url(r'^reset/(?P<pk>.+)$', BinResetView.as_view(), name='reset'),

    url(r'^item/list/(?P<bin_pk>.+)$', BinItemListView.as_view(), name='bin-item-list'),
    url(r'^item/(?P<pk>.+)$', BinItemView.as_view(), name='bin-item'),
    url(r'^item/delete/(?P<pk>.+)$', BinItemDeleteView.as_view(), name='bin-item-delete'),

    #url(r'^update/(?P<pk>.+)$', BinRetriveUpdateView.as_view(), name='update'),
    #url(r'^list/$', BinViewSet.as_view({'get': 'list'}), name='list'),
    #url(r'^retrieve/(?P<pk>.+)$', BinViewSet.as_view({'get': 'retrieve'}), name='retrieve'),


]
