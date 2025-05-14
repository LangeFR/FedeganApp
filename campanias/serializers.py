from rest_framework import serializers
from .models import Campaña, Vacunacion


class CampañaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaña
        fields = '__all__'


class VacunacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacunacion
        fields = '__all__'
