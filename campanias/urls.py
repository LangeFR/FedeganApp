from django.urls import path
from .views import CampañaListView, VacunacionCreateView

urlpatterns = [
    path('campanas/', CampañaListView.as_view(), name='lista-campañas'),
    path('vacunaciones/crear/', VacunacionCreateView.as_view(),
         name='crear-vacunacion'),
]
