from django.conf.urls import url

from .views.view_drill_search import DrillSearchView
from .views.view_simple_search import SimpleSearchView

urlpatterns = [

    url(r'^simple-search/$', SimpleSearchView.as_view(), name='simple-search'),
    url(r'^drill-search/$', DrillSearchView.as_view(), name='drill-search'),

]