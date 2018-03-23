from django.conf.urls import url

from apps.log.views import UserBinLogViewSet

urlpatterns = [

    url(r'^user-search/$', UserBinLogViewSet.as_view({'get': 'list'}), name='user-search'),


]
