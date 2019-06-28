from rest_framework.viewsets import ModelViewSet

from .models import Profile
from .serializers import ProfileSerializers


class ProfileViewSet(ModelViewSet):
    """ Work with marks"""
    serializer_class = ProfileSerializers
    queryset = Profile.objects.all()