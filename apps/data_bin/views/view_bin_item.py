from django.shortcuts import get_object_or_404
from rest_framework import generics

from apps.data_bin.models import BinItem, Bin
from apps.data_bin.serializers import BinItemSerializer, BinItemSimpleSerializer


class BinItemListView(generics.ListAPIView):
    """
    Return 'Bin' list for current user
    """
    serializer_class = BinItemSimpleSerializer
    #permission_classes = (IsAdminUser,)

    def get_queryset(self):
        queryset = Bin.objects.all()
        bin_pk = self.kwargs['bin_pk']
        bin = get_object_or_404(queryset, pk=bin_pk)
        user = self.request.user
        return BinItem.objects.filter(bin=bin)


class BinItemView(generics.RetrieveAPIView):
    """
    Return 'Bin' list for current user
    """
    serializer_class = BinItemSerializer
    #permission_classes = (IsAdminUser,)

    def get_queryset(self):
        pk = self.kwargs['pk']
        #queryset = BinItem.objects.all()
        #bin_item = get_object_or_404(queryset, pk=pk)
        #user = self.request.user
        return BinItem.objects.filter(pk=pk)
