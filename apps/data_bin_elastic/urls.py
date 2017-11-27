from django.conf.urls import url

from .views import DataBinDrillSearchView, DataBinSimpleSearchView

urlpatterns = [

    url(r'^simple-search/$', DataBinSimpleSearchView.as_view(), name='simple-search'),
    url(r'^mapped-search/$', DataBinDrillSearchView.as_view(), name='mapped-search'),

]