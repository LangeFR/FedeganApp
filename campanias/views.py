from .serializers import VacunacionSerializer
from .models import Vacunacion
from .serializers import CampañaSerializer
from .models import Campaña
from rest_framework import generics, permissions
from .models import Campaña, Vacunacion
from .serializers import CampañaSerializer, VacunacionSerializer

# 1. Listar todas las campañas


class CampañaListView(generics.ListAPIView):
    queryset = Campaña.objects.all()
    serializer_class = CampañaSerializer
    # o AllowAny si es público
    permission_classes = [permissions.IsAuthenticated]


class CampañaCreateView(generics.CreateAPIView):
    queryset = Campaña.objects.all()
    serializer_class = CampañaSerializer
    permission_classes = [permissions.IsAuthenticated]


# 2. Crear una nueva vacunación


class VacunacionCreateView(generics.CreateAPIView):
    queryset = Vacunacion.objects.all()
    serializer_class = VacunacionSerializer
    # Asegura que esté autenticado
    permission_classes = [permissions.IsAuthenticated]


class VacunacionListView(generics.ListAPIView):
    queryset = Vacunacion.objects.all()
    serializer_class = VacunacionSerializer
    permission_classes = [permissions.IsAuthenticated]
