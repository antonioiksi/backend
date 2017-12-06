import json
from pprint import pprint

from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import views, status
from rest_framework.test import APIRequestFactory, force_authenticate

from apps.auth_jwt.permissions import PublicEndpoint
from apps.data_bin.views.view_bin import FlatDataBinView
from apps.data_graph.models import GraphData


class LoadGraphFromBinView(views.APIView):
    permission_classes = (PublicEndpoint,)

    def get(self, request, *args, **kwargs):
        bin_pk = self.kwargs['bin_pk']
        user = self.request.user
        factory = APIRequestFactory()
        req = factory.get('/bin/flat-data/'+bin_pk)
        force_authenticate(req, user=user)

        view = FlatDataBinView.as_view()
        res = view(req, pk=bin_pk)
        #pprint(json.loads( resp.body))

        for item in res.data:
            graphData = GraphData(data=item, user=user)
            graphData.save()

        return Response(res.data, status=status.HTTP_200_OK)


class ClearGraphView(views.APIView):
    permission_classes = (PublicEndpoint,)

    def get(self, request, *args, **kwargs):
        user = self.request.user
        count = GraphData.objects.filter(user=user).delete()

        return Response({'deleted':count[0]}, status=status.HTTP_200_OK)