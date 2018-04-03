from django.conf.urls import url

from .views import DataBinSimpleSearchView, ElasticView, CsvView

urlpatterns = [


    url(r'^elastic/(?P<bin_pk>.+)$', ElasticView.as_view(), name='elastic'),
    url(r'^csv/(?P<bin_pk>.+)$', CsvView.as_view(), name='csv'),

    # url(r'^simple-search/$', DataBinSimpleSearchView.as_view(), name='simple-search'),

]
