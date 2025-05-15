from django.urls import path
from .views import AnimalListView, AnimalCreateView

urlpatterns = [
    path('animales/', AnimalListView.as_view(), name='lista-animales'),
    path('animales/crear/', AnimalCreateView.as_view(), name='crear-animal'),
]
