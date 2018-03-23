from django.conf.urls import url

from .views import (AttributeListView, EntityAttributeListView,
                    EntityAttributeMappingListView)

urlpatterns = [

    url(r'^list/$', AttributeListView.as_view()),
    url(r'^list-entity-attribute/$', EntityAttributeListView.as_view()),
    url(r'^list-entity-attribute-mapping/$', EntityAttributeMappingListView.as_view()),

]
