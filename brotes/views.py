from rest_framework import generics, permissions
from .models import Brote
from .serializers import BroteSerializer

# Listar todos los brotes


class BroteListView(generics.ListAPIView):
    queryset = Brote.objects.all()
    serializer_class = BroteSerializer
    # Usa AllowAny si no se requiere autenticación
    permission_classes = [permissions.IsAuthenticated]

# Crear un nuevo brote


class BroteCreateView(generics.CreateAPIView):
    queryset = Brote.objects.all()
    serializer_class = BroteSerializer
    permission_classes = [permissions.IsAuthenticated]
