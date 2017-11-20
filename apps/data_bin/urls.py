from django.conf.urls import url

from apps.data_bin.views.view_bin import BinListView, BinCreateView, BinDeleteView, BinResetView
from apps.data_bin.views.view_bin_item import BinItemListView, BinItemView, BinItemDeleteView

urlpatterns = [

    url(r'^list/$', BinListView.as_view(), name='list'),
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


