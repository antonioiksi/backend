from django.conf.urls import url

from apps.tests.views import TestDRFView, TestDRFESView, TestDRFDataBaseView

urlpatterns = [

    url(r'^drf/$', TestDRFView.as_view(), name='drf'),
    url(r'^drf-postgres/$', TestDRFDataBaseView.as_view(), name='drf-database'),
    url(r'^drf-es/$', TestDRFESView.as_view(), name='drf-es'),

]