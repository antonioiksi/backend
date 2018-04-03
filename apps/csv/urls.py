from django.conf.urls import url

from apps.csv.views import CsvLoadView

urlpatterns = [
    url(r'^load/$', CsvLoadView.as_view(), name='load'),
]
