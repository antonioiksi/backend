from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from apps.data_graph.views.GraphDataView import LoadGraphDataView, ClearGraphDataView, JsonbFilterView, \
    GraphDataByModelNameView, GraphDataAllKeysView
from apps.data_graph.views.GraphNodeEdgeView import GraphNodeEdgeListView, \
    GraphNodeEdgeClearView, GraphNodeEdgeAddForRelationsView
from apps.data_graph.views.GraphModelDrawingView import GraphModelDrawingViewSet
from apps.data_graph.views.GraphModelView import GraphModelViewSet, GraphModelForGraphViewSet
from apps.data_graph.views.GraphNodeView import GraphNodeListView, GraphNodeClearView, GraphNodeAddForModelsView
from apps.data_graph.views.GraphRelationView import GraphRelationViewSet, GraphRelationComparatorsView, \
    GraphRelationForGraphViewSet
from apps.data_graph.views.GraphView import GraphViewSet




urlpatterns = [

    url(r'^clear/(?P<graph_id>.+)$', ClearGraphDataView.as_view(), name='clear'),
    url(r'^load-data/(?P<graph_id>.+)$', LoadGraphDataView.as_view(), name='load-data'),


    url(r'^data-by-object-name/(?P<graph_name>.+)$', GraphDataByModelNameView.as_view(), name='data-by-name'),


    url(r'^node/remove-all/(?P<graph_id>.+)/$', GraphNodeClearView.as_view(), name='node-remove-all'),
    url(r'^node/list/(?P<graph_id>.+)/$', GraphNodeListView.as_view(), name='node-list'),
    url(r'^node/add/(?P<graph_id>.+)/$', GraphNodeAddForModelsView.as_view(), name='node-add'),

    url(r'^edge/remove-all/(?P<graph_id>.+)/$', GraphNodeEdgeClearView.as_view(), name='edge-remove-all'),
    url(r'^edge/list/(?P<graph_id>.+)/$', GraphNodeEdgeListView.as_view(), name='edge-list'),
    url(r'^edge/add/(?P<graph_id>.+)/$', GraphNodeEdgeAddForRelationsView.as_view(), name='edge-add'),

    #url(r'^object/(?P<object_name>.+)$', GraphObjectViewSet.as_view(), name='objects-by-name'),

    url(r'^all-keys/(?P<graph_id>.+)$', GraphDataAllKeysView.as_view(),
        name='all-keys'),
    url(r'^comparators/$', GraphRelationComparatorsView.as_view(),
        name='comparators'),

    url(r'^filter/$', JsonbFilterView.as_view(), name='filter'),

    url(r'^model/for-graph/(?P<graph_id>.+)$', GraphModelForGraphViewSet.as_view(), name='filter'),
    url(r'^relation/for-graph/(?P<graph_id>.+)$', GraphRelationForGraphViewSet.as_view(), name='filter'),

]

router = DefaultRouter()
router.register(r'graph', GraphViewSet, base_name='graph')

router.register(r'model', GraphModelViewSet, base_name='model')

router.register(r'drawing', GraphModelDrawingViewSet, base_name='drawing')

router.register(r'relation', GraphRelationViewSet, base_name='relation')

urlpatterns.extend(router.urls)