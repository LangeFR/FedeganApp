from django.urls import path
from .views import CampañaListView, VacunacionCreateView

urlpatterns = [
    path('campañas/', CampañaListView.as_view(), name='lista-campañas'),
    path('vacunaciones/crear/', VacunacionCreateView.as_view(),
         name='crear-vacunacion'),
]
