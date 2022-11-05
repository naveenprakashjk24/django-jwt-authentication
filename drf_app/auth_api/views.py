from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from auth_api.serializers import UserSerializers
from django.contrib.auth import get_user_model




class UserSerializerView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,]
    serializer_class = UserSerializers
    queryset = get_user_model().objects.all()