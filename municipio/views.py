from rest_framework import generics, permissions
from .models import Municipio
from .serializers import MunicipioSerializer

# 1. Listar todos los municipios


class MunicipioListView(generics.ListAPIView):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer
    # Usa AllowAny si es pública
    permission_classes = [permissions.IsAuthenticated]

# 2. Obtener un municipio por ID


class MunicipioDetailView(generics.RetrieveAPIView):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'
