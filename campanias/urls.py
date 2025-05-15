from django.urls import path
from .views import VacunacionListView, CampañaCreateView, CampañaListView, VacunacionCreateView

urlpatterns = [
    path('campanas/', CampañaListView.as_view(), name='lista-campañas'),
    path('vacunaciones/crear/', VacunacionCreateView.as_view(),
         name='crear-vacunacion'),
    path('campanas/crear/', CampañaCreateView.as_view(), name='crear-campaña'),
    path('vacunaciones/', VacunacionListView.as_view(), name='lista-vacunaciones'),
]
