from rest_framework import generics

from apps.auth_jwt.permissions import PublicEndpoint
from apps.elastic.models import QueryTemplate
from apps.elastic.serializers import QueryTemplateSerializer


class QueryTemplateListView(generics.ListAPIView):
    """
    Return 'Bin' list for current user
    """
    permission_classes = (PublicEndpoint,)
    serializer_class = QueryTemplateSerializer
    queryset = QueryTemplate.objects.all()

    #permission_classes = (IsAdminUser,)

    #def get_queryset(self):
        #user = self.request.user

        #return Bin.objects.filter(user=user)

        #.annotate(
        #    item_count=Count('binitem'),
        #)