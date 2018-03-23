from rest_framework import status, views, viewsets
from rest_framework.response import Response

from apps.attribute.models import EntityAttribute
from apps.auth_jwt.permissions import PublicEndpoint
from apps.data_graph.models import GraphModelDrawing
from apps.data_graph.models.Graph import Graph
from apps.data_graph.models.ModelTemplate import ModelTemplate
from apps.data_graph.serializers.GraphSerializer import GraphSerializer


class CopyDefaultModelTemplatesView(views.APIView):
    # create model template (one field model) for each attribute
    permission_classes = (PublicEndpoint,)

    def get(self, request, *args, **kwargs):
        defaultModelTemplates = ModelTemplate.objects.filter(user=None)
        user = self.request.user

        count = 0
        countErr = 0
        for defaultModelTemplate in defaultModelTemplates:
            templates = ModelTemplate.objects.filter(user=user, name=defaultModelTemplate.name)
            if len(templates) > 0:
                break

            try:
                modelTemplate = ModelTemplate(
                    user=user,
                    name=defaultModelTemplate.name,
                    fields=defaultModelTemplate.fields[:],
                    is_group=defaultModelTemplate.is_group,
                    drawing=defaultModelTemplate.drawing
                )

                modelTemplate.save()
                count += 1
            except Exception:
                print('Exception')
                countErr += 1

        return Response({'Created': count, 'Error': countErr}, status=status.HTTP_200_OK)



class ClearModelTemplateView(views.APIView):
    # delete all ModelTemplate objects for current user
    permission_classes = (PublicEndpoint,)

    def get(self, request, *args, **kwargs):
        user = self.request.user

        deleted = ModelTemplate.objects.filter(user=user).delete()

        return Response({'Deleted': deleted}, status=status.HTTP_200_OK)
