from pprint import pprint

from django.shortcuts import render

# Create your views here.
from rest_framework import views, status, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from apps.auth_jwt.permissions import PublicEndpoint
from apps.data_graph.models import GraphData, GraphObject
from apps.data_graph.serializers import GraphObjectSerializer


class JsonbFilterView(views.APIView):
    '''
    https://docs.djangoproject.com/en/2.0/ref/contrib/postgres/fields/

    '''
    permission_classes = (PublicEndpoint,)

    def get(self, request, *args, **kwargs):
        user = self.request.user
        #pk = self.kwargs['pk']

        arr = GraphData.objects.all()
        #GraphData.objects.filter(data__contains='"_index":"shakespeare"')
        arr1 = GraphData.objects.filter(data__contains={'_id': '40001'})

        GraphData.objects.filter(data__has_keys=['_id', '_index'])

        arr_data = [ item.data for item in arr1]

        return Response(arr_data, status=status.HTTP_200_OK)



class ObjectsByNameView(views.APIView):
    permission_classes = (PublicEndpoint,)

    def get(self, request, *args, **kwargs):
        user = self.request.user
        object_name = self.kwargs['object_name']

        try:
            object = GraphObject.objects.get(name=object_name)
        except:
            return Response(None, status=status.HTTP_204_NO_CONTENT)

        objects = GraphData.objects.filter(data__has_keys=object.fields)
        arr_data = []
        if len(objects)>0:
            arr_data = [item.data for item in objects]
        return Response(arr_data, status=status.HTTP_200_OK)


class GraphObjectViewSet(viewsets.ViewSet):
    permission_classes = (PublicEndpoint,)

    def list(self, request):
        queryset = GraphObject.objects.all()
        serializer = GraphObjectSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        queryset = GraphObject.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = GraphObjectSerializer(user)
        return Response(serializer.data)

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass

