from pprint import pprint

from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework import generics, viewsets, views, status
from rest_framework.generics import GenericAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from apps.data_bin.models import Bin, BinItem
from apps.data_bin.serializers import BinSerializer


class BinListView(generics.ListAPIView):
    """
    Return 'Bin' list for current user
    """
    serializer_class = BinSerializer
    #permission_classes = (IsAdminUser,)

    def get_queryset(self):
        user = self.request.user
        return Bin.objects.filter(user=user)


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

        # TODO add removing BinItems belong to Bin
        BinItem.objects.filter(bin=bin).delete()

        serializer = BinSerializer(bin)
        return Response(serializer.data)

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