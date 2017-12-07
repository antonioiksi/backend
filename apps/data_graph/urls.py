from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from apps.data_graph.views.view_graph_data import LoadGraphDataView, GraphDataByObjectNameView, ClearUserGraphDataView
from .views.view_graph_object import JsonbFilterView, GraphObjectViewSet

urlpatterns = [

    url(r'^filter/$', JsonbFilterView.as_view(), name='filter'),
    url(r'^data-by-object-name/(?P<object_name>.+)$', GraphDataByObjectNameView.as_view(), name='objects-by-name'),
    url(r'^load-data$', LoadGraphDataView.as_view(), name='load-data'),
    url(r'^clear$', ClearUserGraphDataView.as_view(), name='clear'),

    #url(r'^object/(?P<object_name>.+)$', GraphObjectViewSet.as_view(), name='objects-by-name'),

]

router = DefaultRouter()
router.register(r'object', GraphObjectViewSet, base_name='object')
urlpatterns.extend(router.urls)