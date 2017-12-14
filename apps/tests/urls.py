from django.conf.urls import url

from apps.tests.views import TestDRFView, TestDRFESView

urlpatterns = [

    url(r'^drf/$', TestDRFView.as_view(), name='drf'),
    url(r'^drf-postgres/$', TestDRFESView.as_view(), name='drf-postgres'),
    url(r'^drf-es/$', TestDRFESView.as_view(), name='drf-es'),

]