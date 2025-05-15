from django.urls import path
from .views import MunicipioListView, MunicipioDetailView

urlpatterns = [
    path('municipios/', MunicipioListView.as_view(), name='lista-municipios'),
    path('municipios/<int:id>/', MunicipioDetailView.as_view(),
         name='detalle-municipio'),
]
