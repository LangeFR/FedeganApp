from django.urls import path
from .views import BroteListView, BroteCreateView

urlpatterns = [
    path('brotes/', BroteListView.as_view(), name='lista-brotes'),
    path('brotes/crear/', BroteCreateView.as_view(), name='crear-brote'),
]
