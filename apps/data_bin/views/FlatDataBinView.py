from rest_framework import generics, status, views, viewsets
from rest_framework.response import Response

from apps.auth_jwt.permissions import PublicEndpoint
from apps.data_bin.models import Bin, BinItem
from apps.data_bin.utils import flatten


class FlatDataBinView(views.APIView):
    """
    Get data from Items by Bin's Id (flat json mode)
    """
    permission_classes = (PublicEndpoint,)

    def get(self, request, *args, **kwargs):
        queryset = Bin.objects.all()
        user = self.request.user
        pk = self.kwargs['pk']
        bin = Bin.objects.get(pk=pk)

        # if user!=bin.user:
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
            # allData.extend(itemData.data)

        # flatten json
        flatData = [
            flatten(data)
            for data in allData]
        # list = [
        # {'_id':item['_id'] for item in binItem.data}
        # binItem.data
        #    for binItem in BinItem.objects.filter(bin=bin)]

        # temp = [{'_id':1,'name':'n1'},{'_id':2,'name':'n2'}]

        return Response(flatData, status=status.HTTP_200_OK)
        # return Response(temp, status=status.HTTP_200_OK)
