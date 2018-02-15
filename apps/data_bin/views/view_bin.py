from pprint import pprint

from django.db.models import Count
from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework import generics, viewsets, views, status
from rest_framework.generics import GenericAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from apps.auth_jwt.permissions import PublicEndpoint
from apps.data_bin.models import Bin, BinItem
from apps.data_bin.serializers import BinSerializer, BinItemSimpleSerializer
from apps.data_bin.utils import flatten


class BinListView(generics.ListAPIView):
    """
    Return 'Bin' list for current user
    """
    serializer_class = BinSerializer
    #permission_classes = (IsAdminUser,)

    def get_queryset(self):
        user = self.request.user

        return Bin.objects.filter(user=user)

        #.annotate(
        #    item_count=Count('binitem'),
        #)

class ActiveBinRetrieveView(GenericAPIView):
    """
    Return active 'Bin' for current user
    """
    #permission_classes = (IsAdminUser,)

    def get(self, request, pk=None):
        user = self.request.user
        queryset = Bin.objects.filter(user=user)
        bin = get_object_or_404(queryset, active=True)

        serializer = BinSerializer(bin)
        return Response(serializer.data)



class BinCreateView(generics.CreateAPIView):
    serializer_class = BinSerializer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BinDeleteView(generics.DestroyAPIView):
    serializer_class = BinSerializer


class BinResetView(GenericAPIView):
    def get(self, request, pk=None):
        queryset = Bin.objects.all()
        bin = get_object_or_404(queryset, pk=pk)

        # add removing BinItems belong to Bin
        BinItem.objects.filter(bin=bin).delete()

        serializer = BinSerializer(bin)
        return Response(serializer.data)


class BinActivateView(views.APIView):

    def get(self, request, *args, **kwargs):
        name = self.kwargs['name']
        user = self.request.user

        bin = Bin.objects.get(name=name, user=user)
        Bin.objects.filter(user=user).update(active=False)
        bin.active = True
        bin.save()

        list = [BinSerializer(bin).data for bin in Bin.objects.filter(user=user)]
        #serializer = BinSerializer(bin)
        #return Response(json.dumps( serializer.data, ensure_ascii=False), status=status.HTTP_200_OK)
        #return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(list, status=status.HTTP_200_OK)




class FlatDataBinView(views.APIView):
    permission_classes = (PublicEndpoint,)

    def get(self, request, *args, **kwargs):
        queryset = Bin.objects.all()
        user = self.request.user
        pk = self.kwargs['pk']
        bin = Bin.objects.get(pk=pk)

        #if user!=bin.user:
        #    return Response({'error':'you are not a bin\'s owner!'}, status=status.HTTP_403_FORBIDDEN)

        ids = []
        allData = []

        # distinct json
        for itemData in BinItem.objects.filter(bin=bin):
            for item in itemData.data:
                id = item['_id']
                if id not in ids:
                    allData.append(item)
                    ids.append(id)
            #allData.extend(itemData.data)

        # flatten json
        flatData = [
            flatten(data)
                    for data in allData]
        #list = [
            #{'_id':item['_id'] for item in binItem.data}
            #binItem.data
            #    for binItem in BinItem.objects.filter(bin=bin)]

        #temp = [{'_id':1,'name':'n1'},{'_id':2,'name':'n2'}]

        return Response(flatData, status=status.HTTP_200_OK)
        #return Response(temp, status=status.HTTP_200_OK)

"""
class BinRetriveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Bin.objects
    serializer_class = BinSerializer
    def perform_update(self, serializer):
        instance = serializer.save(user=self.request.user)
        #send_email_confirmation(user=self.request.user, modified=instance)
"""

"""
class BinViewSet(viewsets.ViewSet):
    def list(self, request):
        user = request.user
        queryset = Bin.objects.all()
        #serializer = BinSerializer(queryset, many=True)
        serializer = BinSerializer(queryset)
        json = JSONRenderer().render(serializer.data)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Bin.objects.all()
        bin = get_object_or_404(queryset, pk=pk)
        serializer = BinSerializer(bin)
        return Response(serializer.data)
"""