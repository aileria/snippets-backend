from rest_framework import permissions
from shared.views import BaseModelViewSet
from .serializers import TopicSerializer
from .models import Topic


class TopicViewSet(BaseModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

    permission_classes_by_action = {
        "create": (permissions.IsAuthenticated,),
        "update": (permissions.IsAuthenticated,),
        'partial_update': (permissions.IsAuthenticated,),
        "destroy": (permissions.IsAuthenticated,),
    }
