from rest_framework import serializers
from .models import Brote


class BroteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brote
        fields = '__all__'
