from rest_framework import generics, permissions
from .models import Animal
from .serializers import AnimalSerializer

# Listar todos los animales


class AnimalListView(generics.ListAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    # O usa AllowAny si es público
    permission_classes = [permissions.IsAuthenticated]

# Crear un nuevo animal


class AnimalCreateView(generics.CreateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    permission_classes = [permissions.IsAuthenticated]
