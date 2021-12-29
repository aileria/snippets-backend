from rest_framework import permissions
from shared.permissions import IsOwner
from shared.views import BaseModelViewSet
from .serializers import UserSerializer
from .models import User


class UserViewSet(BaseModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes_by_action = {
        "create": (permissions.IsAdminUser | IsOwner,),
        "update": (permissions.IsAdminUser | IsOwner,),
        'partial_update': (permissions.IsAdminUser | IsOwner,),
        "destroy": (permissions.IsAdminUser | IsOwner,),
    }
