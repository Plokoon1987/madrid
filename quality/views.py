from django.contrib.auth.models import User, Group
from . import models

from rest_framework import viewsets
from rest_framework import permissions
from . import serializers


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class EstacionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Estacion.objects.all().order_by('provincia', 'municipio', 'estacion')
    serializer_class = serializers.EstacionSerializer
    permission_classes = [permissions.IsAuthenticated]


class DiaMedicionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.DiaMedicion.objects.all().order_by('-ano', '-mes', '-dia')
    serializer_class = serializers.DiaMedicionSerializer
    permission_classes = [permissions.IsAuthenticated]


class HoraMedicionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.HoraMedicion.objects.all().order_by('hora')
    serializer_class = serializers.HoraMedicionSerializer
    permission_classes = [permissions.IsAuthenticated]
