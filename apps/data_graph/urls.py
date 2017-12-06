from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from .views import JsonbFilterView, ObjectsByNameView, GraphObjectViewSet

urlpatterns = [

    url(r'^filter/$', JsonbFilterView.as_view(), name='filter'),
    url(r'^objects-by-name/(?P<object_name>.+)$', ObjectsByNameView.as_view(), name='objects-by-name'),
    #url(r'^object/(?P<object_name>.+)$', GraphObjectViewSet.as_view(), name='objects-by-name'),

]

router = DefaultRouter()
router.register(r'object', GraphObjectViewSet, base_name='object')
urlpatterns.extend(router.urls)