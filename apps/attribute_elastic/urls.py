from django.conf.urls import url

from .views import AddedMappedFieldListView

urlpatterns = [

    url(r'^reload-mapped-attributes/$', AddedMappedFieldListView.as_view(), name='reload-mapped-attributes'),

]