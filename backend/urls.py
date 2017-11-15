"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views import generic
from rest_framework.schemas import get_schema_view

urlpatterns = [
    # redirect
    url(r'^$', generic.RedirectView.as_view(url='/api/', permanent=False)),
    url(r'^admin/', admin.site.urls),

    url(r'^api/$', get_schema_view()),

    # JWT authentification
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^auth/', include('apps.auth_jwt.urls', namespace='auth_jwt')),

    #
    url(r'^elastic/', include('apps.elastic.urls', namespace='elastic')),

    #
    url(r'^bins/', include('apps.data_bin.urls', namespace='data_bin')),

    #
    url(r'^elastic-bins/', include('apps.data_bin_elastic.urls', namespace='elastic')),

    #
    url(r'^attribute/', include('apps.attribute.urls', namespace='attribute')),
]