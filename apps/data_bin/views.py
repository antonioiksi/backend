from pprint import pprint

from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework import generics, viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from .serializers import BinSerializer
from .models import Bin


class BinViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
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



class BinListCreate(generics.ListCreateAPIView):
    queryset = Bin.objects.filter()
    serializer_class = BinSerializer
    #permission_classes = (IsAdminUser,)

"""
    def list(self, request):
        print('aaa')
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        #serializer = BinSerializer(queryset, many=True)
        serializer = BinSerializer(queryset, user=request.user)
        return Response(serializer.data)
"""
"""
class BinCreate(generics.CreateAPIView):

    serializer_class = BinSerializer

    def perform_create(self, serializer):
        serializer.save()
"""

class BinRetriveUpdate(generics.RetrieveUpdateAPIView):
    queryset = Bin.objects
    serializer_class = BinSerializer

    def perform_update(self, serializer):
        instance = serializer.save()
        #send_email_confirmation(user=self.request.user, modified=instance)

