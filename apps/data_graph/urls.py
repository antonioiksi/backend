from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from apps.data_graph.views.GraphDataView import LoadGraphDataView, ClearGraphDataView, JsonbFilterView, \
    GraphDataByModelNameView
from apps.data_graph.views.GraphEdgeView import GraphEdgesByRelationsView
from apps.data_graph.views.GraphModelView import GraphModelViewSet
from apps.data_graph.views.GraphNodeView import GraphNodesByModelsView, GraphNodeListView
from apps.data_graph.views.GraphRelationView import GraphRelationViewSet
from apps.data_graph.views.GraphView import GraphViewSet, GraphActivateView

urlpatterns = [

    url(r'^activate/(?P<name>.+)$', GraphActivateView.as_view(), name='activate'),
    url(r'^clear/(?P<graph_name>.+)$', ClearGraphDataView.as_view(), name='clear'),
    url(r'^load-data/(?P<graph_name>.+)$', LoadGraphDataView.as_view(), name='load-data'),

    url(r'^filter/$', JsonbFilterView.as_view(), name='filter'),
    url(r'^data-by-object-name/(?P<graph_name>.+)$', GraphDataByModelNameView.as_view(), name='data-by-name'),


    url(r'^node/list/(?P<graph_name>.+)/$', GraphNodeListView.as_view(), name='node-list'),
    url(r'^node/(?P<action>.+)/(?P<graph_name>.+)/$', GraphNodesByModelsView.as_view(), name='node-save'),

    url(r'^edge/(?P<graph_name>.+)$', GraphEdgesByRelationsView.as_view(),
        name='edge'),

    #url(r'^object/(?P<object_name>.+)$', GraphObjectViewSet.as_view(), name='objects-by-name'),

]

router = DefaultRouter()
router.register(r'viewset', GraphViewSet, base_name='graph')

router.register(r'model', GraphModelViewSet, base_name='model')

router.register(r'relation', GraphRelationViewSet, base_name='relation')

urlpatterns.extend(router.urls)