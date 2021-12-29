from rest_framework import permissions
from shared.views import BaseModelViewSet
from .serializers import UserSerializer
from .models import User

class UserViewSet(BaseModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    permission_classes_by_action = {
        "create": (permissions.IsAuthenticated,),
        "update": (permissions.IsAuthenticated,),
        'partial_update': (permissions.IsAuthenticated,),
        "destroy": (permissions.IsAuthenticated,),
    }
