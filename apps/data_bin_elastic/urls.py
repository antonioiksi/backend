from django.conf.urls import url

from .views import DataBinDrillSearchView

urlpatterns = [

    url(r'^drill-search/$', DataBinDrillSearchView.as_view(), name='drill-search'),

]