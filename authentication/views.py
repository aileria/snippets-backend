from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer
from rest_framework import generics
from django.contrib.auth import get_user_model

User = get_user_model()


@extend_schema_view(
    post=extend_schema(description='Registers a user and returns an access and refresh JSON web token pair.'),
)
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
