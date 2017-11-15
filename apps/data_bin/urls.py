from django.conf.urls import url

from .views import BinListCreate, BinRetriveUpdate

urlpatterns = [

    url(r'^list/$', BinListCreate.as_view(), name='list'),
    url(r'^update/(?P<pk>.+)$', BinRetriveUpdate.as_view(), name='update'),

    #url(r'^list/$', BinViewSet.as_view({'get': 'list'}), name='list'),
    #url(r'^retrieve/(?P<pk>.+)$', BinViewSet.as_view({'get': 'retrieve'}), name='retrieve'),


]


