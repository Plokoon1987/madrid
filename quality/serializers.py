from django.contrib.auth.models import User, Group
from . import models
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class EstacionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Estacion
        fields = ['url', 'provincia', 'municipio', 'estacion']


class DiaMedicionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.DiaMedicion
        fields = ['url', 'estacion_id', 'estacion', 'ano', 'mes', 'dia', 'magnitud', 'punto_muestreo']


class HoraMedicionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.HoraMedicion
        fields = ['url', 'dia_medicion_id', 'dia_medicion', 'hora', 'cantidad', 'validacion']
