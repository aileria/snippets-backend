from rest_framework import permissions
from shared.views import BaseModelViewSet
from .serializers import TechnologySerializer
from .models import Technology

class TechnologyViewSet(BaseModelViewSet):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer
    
    permission_classes_by_action = {
        "create": (permissions.IsAuthenticated,),
        "update": (permissions.IsAuthenticated,),
        'partial_update': (permissions.IsAuthenticated,),
        "destroy": (permissions.IsAuthenticated,),
    }