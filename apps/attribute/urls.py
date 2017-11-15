from django.conf.urls import url

from .views import AttributeListView

urlpatterns = [

    url(r'^list/$', AttributeListView.as_view()),

]